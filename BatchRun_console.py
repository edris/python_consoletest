import os
import glob
import subprocess
import argparse
import csv

def run_script_on_all_csv_files(directory, script_name):
    """
    Run the provided script on all CSV files in the specified directory.
    :param directory: Path to the directory containing CSV files.
    :param script_name: Name of the Python script to run on each CSV file.
    """
    # Open CSV files for logging
    with open(skip_file, mode='w', newline='') as skip_f, open(error_file, mode='w', newline='') as error_f, open(send_file, mode='w', newline='') as send_f:

        skip_writer = csv.writer(skip_f)
        error_writer = csv.writer(error_f)
        send_writer = csv.writer(send_f)
        # Get a list of all CSV files in the directory
        csv_files = glob.glob(os.path.join(directory, '*.csv'))

        # Run the script on each CSV file
        #for csv_file in csv_files:
        #    print(f"Running {script_name} on {csv_file}...")
        #    subprocess.run(['python3', script_name, csv_file])
        for csv_file in csv_files:
            print(f"Running {script_name} on {csv_file}...")
            result = subprocess.run(['python3', script_name, csv_file], capture_output=True, text=True)

            # Process the output and write to respective CSV files
            for line in result.stdout.splitlines():
                if "Skipping" in line:
                    skip_writer.writerow([csv_file, line])
                elif "Error" in line:
                    error_writer.writerow([csv_file, line])
                elif "Message sent" in line:
                    send_writer.writerow([csv_file, line])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a script on all CSV files in a specified directory.")
    parser.add_argument("directory", help="Directory containing CSV files")
    args = parser.parse_args()

    # File paths for logging results
    skip_file = 'skipped_messages.csv'
    error_file = 'error_messages.csv'
    send_file = 'sent_messages.csv'

    # The script assumes that 'send_can_messages.py' is in the current working directory
    run_script_on_all_csv_files(args.directory, 'python_consoletest.py')
