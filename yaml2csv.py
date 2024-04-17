# First run
# > pip install pyyaml

import yaml
import csv
import sys

def yaml_to_csv(yaml_file, csv_file):
    # Load the YAML file
    with open(yaml_file, 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
            return

    # Open the CSV file and write the data
    with open(csv_file, 'w', newline='') as file:
        if data is None:
            return
        if not all(isinstance(item, dict) for item in data):
            print("Error: Each item in the YAML file must be a dictionary.")
            return

        # Assuming each dictionary in the list has the same keys
        fields = data[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fields)

        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_yaml_file> <output_csv_file>")
        sys.exit(1)

    input_yaml_file = sys.argv[1]
    output_csv_file = sys.argv[2]

    yaml_to_csv(input_yaml_file, output_csv_file)
