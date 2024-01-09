import os
import glob
import subprocess
import argparse

def run_script_on_all_csv_files(directory, script_name):
    """
    Run the provided script on all CSV files in the specified directory.
    :param directory: Path to the directory containing CSV files.
    :param script_name: Name of the Python script to run on each CSV file.
    """
    # Get a list of all CSV files in the directory
    csv_files = glob.glob(os.path.join(directory, '*.csv'))

    # Run the script on each CSV file
    for csv_file in csv_files:
        print(f"Running {script_name} on {csv_file}...")
        subprocess.run(['python3', script_name, csv_file])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a script on all CSV files in a specified directory.")
    parser.add_argument("directory", help="Directory containing CSV files")
    args = parser.parse_args()

    # The script assumes that 'send_can_messages.py' is in the current working directory
    run_script_on_all_csv_files(args.directory, 'python_consoletest.py')
