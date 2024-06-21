from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
import subprocess
import shlex
import os
import requests
import random 
import string
from tree_sitter_languages import get_language, get_parser
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def fetch_config():
    """
    Fetches the configuration for the current directory from the SQLite database using an absolute path.
    Returns:
        tuple: Returns a tuple containing the virtual environment path and the test directory path.
    """
    # Construct an absolute path to the config database
    base_dir = os.path.abspath(os.path.dirname(__file__))  # This uses the directory of the current file
    config_db_path = os.path.join(base_dir, ".momentum", "config.db")
    print("\nconfig_db_path", config_db_path)
    
    # Connect to the SQLite database to fetch the current directory from runtime_info
    conn = sqlite3.connect(config_db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT file_dir FROM runtime_info")
    runtime_info = cursor.fetchone()
    if runtime_info:
        current_dir = runtime_info[0]
    else:
        raise Exception("Runtime directory information not found. Please ensure the server is initialized correctly.")
    print("\ncurrent_dir", current_dir)
    
    # Fetch the configuration for the current directory
    cursor.execute("SELECT venv_path, test_path FROM config WHERE dir_name = ?", (current_dir,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row
    else:
        raise Exception("Configuration not found. Please ensure Momentum CLI is initialized.")
class Tests(BaseModel):
    content: str
    project_id: str

class DebugTests(BaseModel):
    content: str
    error: str


def parse_pytest_output(output):
    tests = {}
    current_test_name = None
    error_message = []
    output = output.split('\n')

    for line in output:
        if line.startswith('tests/') and '::' in line:
            # Test name found outside the failures section, indicating a new test
            test_name = line.strip()
            test_name = test_name.split('::')[1].split(' ')[0]
            if test_name not in tests:
                tests[test_name] = {
                    'name': test_name,
                    'params': '',
                    'status': 'PASS',  # Assume pass initially
                    'failure_type': '',
                    'stacktrace': ''
                }
        if 'FAILURES ====' in line or 'ERRORS ====' in line:
            # Reset current test name at the start of the failures or errors section
            current_test_name = None
        if line.startswith('____') :
            if current_test_name and current_test_name in tests:
                tests[current_test_name]['stacktrace'] = '\n'.join(error_message)
                error_message = []
                current_test_name = None
            # Indicates a test name within the failures or errors section
            if " ERROR at " in line:
                simplified_test_name = line.strip("_ ").split(" ")[-1]
            else:
                simplified_test_name = line.strip('_ ')
            # Check if this test is already in the list using substring matching
            matched_test = None
            for test_name, test_details in tests.items():
                if simplified_test_name in test_name:
                    matched_test = test_details
                    break
            if matched_test:
                current_test_name = matched_test['name']
                matched_test['status'] = 'ERROR' if ' ERROR ' in line else 'FAIL'
                error_message = []  # Prepare to collect its error message
            else:
                # If the test is not in the list, it's a failure or error without an initial pass status
                # This case should ideally not occur if all tests are captured correctly initially
                current_test_name = simplified_test_name
                tests[current_test_name] = {
                    'name': current_test_name,
                    'params': '',
                    'status': 'FAIL' if 'FAILURES ====' in line else 'ERROR',
                    'failure_type': '',
                    'stacktrace': ''
                }
        if current_test_name and (line.startswith('E   ') or line.startswith('F   ') or not line.startswith('===================')):
            # Collect error messages for the current failed or errored test
            error_message.append(line)
        if line.startswith('===================') and current_test_name:
            # End of the current test's error message
            if current_test_name in tests:
                tests[current_test_name]['stacktrace'] = '\n'.join(error_message)
            current_test_name = None  # Reset for the next test

    # Convert tests dictionary back to list for the output
    tests_list = list(tests.values())

    # Determine the overall test result based on individual test statuses
    if all(test['status'] == 'PASS' for test in tests_list):
        test_result = 'passed'
    elif any(test['status'] == 'ERROR' for test in tests_list):
        test_result = 'errored'
    else:
        test_result = 'failed'

    return {
        'message': f'Tests {test_result}.',
        'details': tests_list
    }

@app.post("/run-tests/")
async def run_tests(test_file: Tests, identifier: str):
    venv_path, test_path = fetch_config() 
    print("\nvenv_path", venv_path)
    print("\ntest_path", test_path)
    test_filepath = await create_temp_test_file(identifier, test_file.content, test_path)  # Pass test_path to the function

    try:
        test_filename = test_filepath.split("/")[-1]

        if not (test_filename.endswith("_test.py") or test_filename.startswith("test")):
            raise HTTPException(status_code=400, detail="Invalid test file name. File should start or end with 'test.py'.")

        # Construct the pytest command using the fetched venv_path
        venv_command = f". {venv_path}/bin/activate"
        pytest_command = f"pytest -vv {shlex.quote(test_filepath)}"
        full_command = f"{venv_command} && which python && {pytest_command}"

        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, executable='/bin/bash')

        if result.stdout:
            print(f"stdout {result.stdout}")
            details = parse_pytest_output(result.stdout)
        else:
            print(f"stderr {result.stderr}")
            return {"message": "Tests failed.", "details": result.stderr}

        if result.returncode == 0:
            return {"message": "Tests ran successfully.", "details": details}
        else:
            return {"message": "Tests failed.", "details": details}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(test_filepath)

@app.post("/add-tests/")
async def add_tests(test_file: Tests, identifier: str):
    try:
        _, test_path = fetch_config()  # Fetch paths from config
        print("\ntest_path", test_path)
        test_filepath = await create_temp_test_file(identifier, test_file.content, test_path)
        test_filename = test_filepath.split("/")[-1]

        return {"filename": test_filename,
                "filepath": test_filepath}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/count-pytest-tests")
async def count_pytest_tests():
    """
    Endpoint to count the number of pytest test functions in the current repository.
    Returns:
        JSON response with the count of pytest test functions or an error message.
    """
    try:
        _, test_path = fetch_config()  # Fetch paths from config
        test_count = count_pytest_tests_in_repo(test_path)
        return {"pytest_test_count": test_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to count pytest tests: {str(e)}")


@app.post("/self-heal-tests/")
async def self_heal_tests(test_file: Tests, identifier: str, authorization: str = Header(None)):
    try:
        _, test_path = fetch_config()  # Fetch paths from config
        print("\ntest_path", test_path)
        test_filepath = await create_temp_test_file(identifier, test_file.content, test_path)
        test_filename = test_filepath.split("/")[-1]

        if not (test_filename.endswith("_test.py") or test_filename.startswith("test")):
            raise HTTPException(status_code=400, detail="Invalid test file name. File should start or end with 'test.py'.")

        # Run the tests and parse the pytest output
        details = await run_tests(test_file, identifier)

        # If tests failed or errored, attempt to self-heal
        if details['message'] != 'Tests passed.':
            # Get the code context and error details

            error_details = "\n".join([test.get('stacktrace', '') for test in details['details']['details'] if test.get('status') != 'PASS'])
            print(identifier)
            # Call the debug_tests function to get the debug information and proposed solution
            final_code = requests.post(
                f"https://staging.momentum.sh/self-heal-tests?identifier={identifier}",
                json={"content": test_file.content, "error": details, "project_id": test_file.project_id},
                headers={"Authorization": authorization}
            ).text

            return final_code
        else:
            return test_file.content

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(test_filepath)


async def create_temp_test_file(identifier, result, test_path):
    temp_file_id = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    if not os.path.exists(test_path):
        os.mkdir(test_path)

    filename = f"{test_path}/test_{identifier.split(':')[-1]}_{temp_file_id}.py"

    with open(filename, 'w') as file:
        file.write(result)
    return filename

def count_pytest_tests_in_repo(repo_path):
    """
    Counts the number of pytest test functions in a given Python repository.
    Args:
    repo_path (str): Path to the Python repository.

    Returns:
    int: Number of pytest test functions.
    """

    print("\nrepo_path", repo_path)
    PY_LANGUAGE = get_language('python')
    parser = get_parser('python')

    test_count = 0

    # Walk through the files in the repository
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py") and file.startswith("test"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    source_code = f.read()

                # Parse the file
                tree = parser.parse(bytes(source_code, "utf8"))
                root_node = tree.root_node

                # Traverse the syntax tree
                query = PY_LANGUAGE.query("""
                    (function_definition
                      name: (identifier) @function-name
                      parameters: (parameters) @params)
                """)

                captures = query.captures(root_node)
                for capture in captures:
                    node, capture_name = capture
                    if capture_name == 'function-name' and node.text.startswith(b'test_'):
                        test_count += 1
    print(test_count)
    return test_count