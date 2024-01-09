import can
import csv
import argparse

class CanBusAdapter:
    # ... [Your existing CanBusAdapter class code] ...

    def parse_message_string(message_string):
        """
        Convert a string representation of a message into a list of integers.
        :param message_string: A string of hexadecimal numbers separated by spaces.
        :return: A list of integers.
        """
        return [int(byte, 16) for byte in message_string.split()]

    def read_and_send_messages(csv_file, can_adapter, allowed_ids):
        """
        Read messages from a CSV file and send them using the provided CAN adapter.
        :param csv_file: Path to the CSV file.
        :param can_adapter: An instance of CanBusAdapter.
        :param allowed_ids: A list of allowed message IDs.
        """
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 2:
                    print("less than two rows")
                    continue  # Skip rows with insufficient data
                try:
                    message_id = int(row[0], 16)  # Assuming ID is in hexadecimal
                    if message_id not in allowed_ids:
                        print(f"Skipping message with disallowed ID: {hex(message_id)}")
                        continue
                    message_data = parse_message_string(row[1])
                    can_adapter.send_obdii_message(message_id, message_data)
                    print("Sending MsgID, DATA: ",message_id, message_data)
                except ValueError as e:
                    print(f"Error processing row {row}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send CAN messages from a CSV file.")
    parser.add_argument("csv_file", help="Path to the CSV file with CAN messages")
    args = parser.parse_args()

    # List of allowed message IDs
    allowed_ids = [0x158, 0x5f2, 0x666, 0x6eb]

    # Replace 'YOUR_CHANNEL' and 'YOUR_INTERFACE' with your actual hardware details
    can_adapter = CanBusAdapter('YOUR_CHANNEL', 'YOUR_INTERFACE')
    read_and_send_messages(args.csv_file, can_adapter, allowed_ids)
