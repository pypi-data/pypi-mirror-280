import typer
import os
import uvicorn
import subprocess
import sys
import sqlite3
cli = typer.Typer()


@cli.command()
def init():
    # Create the necessary directories and files
    base_dir = os.path.abspath(os.path.dirname(__file__))
    momentum_dir = os.path.join(base_dir, ".momentum")
    os.makedirs(momentum_dir, exist_ok=True)

    # Get the current directory name
    print("reg:", os.getcwd())
    current_dir = os.path.basename(os.getcwd())

    # Connect to the SQLite database (or create it if it doesn't exist)
    config_db_path = os.path.join(momentum_dir, "config.db")
    conn = sqlite3.connect(config_db_path)
    cursor = conn.cursor()

    # Create the config table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            dir_name TEXT PRIMARY KEY,
            venv_path TEXT,
            test_path TEXT
        )
    """)

    # Check if the current directory already exists in the database
    cursor.execute("SELECT * FROM config WHERE dir_name = ?", (current_dir,))
    row = cursor.fetchone()

    if row is None:
        # If the current directory doesn't exist in the database, prompt for user input
        venv_path = typer.prompt("Enter the virtual environment path for this directory")
        test_path = typer.prompt("Enter the test dir path for this directory ")

        # Insert the new row into the config table
        cursor.execute("INSERT INTO config (dir_name, venv_path, test_path) VALUES (?, ?, ?)",
                       (current_dir, venv_path, test_path))
        conn.commit()
        typer.echo("Momentum CLI initialized successfully.")
    else:
        typer.echo("Momentum CLI is already initialized for the current directory.")

    conn.close()
    run()

@cli.command()
def config():
    # Get the current directory name
    base_dir = os.path.abspath(os.path.dirname(__file__))
    momentum_dir = os.path.join(base_dir, ".momentum")
    os.makedirs(momentum_dir, exist_ok=True)
    current_dir = os.path.basename(os.getcwd())

    # Connect to the SQLite database
    conn = sqlite3.connect(f"{momentum_dir}/config.db")
    cursor = conn.cursor()

    try:
        # Retrieve the config values for the current directory
        cursor.execute("SELECT * FROM config WHERE dir_name = ?", (current_dir,))
        
    except sqlite3.OperationalError:
        typer.echo("Momentum CLI is not initialized for the current repository.")
        init()
        
    row = cursor.fetchone()
    if row is None:
        typer.echo("Momentum CLI is not initialized for the current repository.")
        init()

    else:
        _, venv_path, test_path = row

        # Prompt for new values (press Enter to keep the existing value)
        new_venv_path = typer.prompt("Enter the new virtual environment path (or Enter to keep the existing value)", default=venv_path)
        new_test_path = typer.prompt("Enter the new test path (or Enter to keep the existing value)", default=test_path)

        # Update the config values in the database
        cursor.execute("UPDATE config SET venv_path = ?, test_path = ? WHERE dir_name = ?",
                       (new_venv_path, new_test_path, current_dir))
        conn.commit()
        typer.echo("Momentum CLI configuration for current repository updated successfully.")

    conn.close()

@cli.command()
def run():
    current_dir = os.path.basename(os.getcwd())
    # Get the directory of the current script
    base_dir = os.path.abspath(os.path.dirname(__file__))
    momentum_dir = os.path.join(base_dir, ".momentum")
    os.makedirs(momentum_dir, exist_ok=True)
    # Connect to the SQLite database
    conn = sqlite3.connect(f"{momentum_dir}/config.db")
    cursor = conn.cursor()

    # Create or update the current directory path in the database
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runtime_info (
            id INTEGER PRIMARY KEY,
            file_dir TEXT
        )
    """)
    cursor.execute("DELETE FROM runtime_info")  # Ensure only one entry exists
    cursor.execute("INSERT INTO runtime_info (file_dir) VALUES (?)", (current_dir,))
    conn.commit()

    # Add the directory containing the 'momentum_cli' module to the Python path
    sys.path.append(base_dir)
    
    # Start the FastAPI server in a detached process
    try:
        subprocess.Popen(["uvicorn", "test_runner:app", "--host", "0.0.0.0", "--port", "5001", "--log-level", "error"], cwd=base_dir)
        typer.echo("Momentum CLI server started.")
    except ModuleNotFoundError:
        typer.echo("Failed to import test_runner. Please make sure the file exists and is properly configured.")

    conn.close()
@cli.command()
def stop():
    # Stop the running FastAPI server instance
    try:
        output = subprocess.check_output(["lsof", "-t", "-i:5001"])
        pids = output.decode().strip().split("\n")
        for pid in pids:
            subprocess.run(["kill", "-9", pid])
        typer.echo("Momentum CLI server stopped.")
    except subprocess.CalledProcessError:
        typer.echo("No running Momentum CLI server found.")
        
if __name__ == "__main__":
    cli()