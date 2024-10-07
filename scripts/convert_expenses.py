import csv
import os

# Folder containing the .txt files to merge into a single csv file
input_folder = "finance/receipts_from_last_night/"
output_file = "finance/receipts_from_last_night/mergedCSV.csv"

# List to store parsed data
data = []

def parse_txt_file(file_path):
    record = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("Employee:"):
                    record['employee_id'] = (line.replace("Employee:", "").strip())
                    # record['employee_id'] = int(record['employee_id'][0])
                elif line.startswith("Items:"):
                    continue
                elif line.startswith("Unit Price:"):
                    try:
                        record['unit_price'] = float(line.replace("Unit Price:", "").strip())
                    except ValueError:
                        print(f"Invalid unit price in file: {file_path}")
                        return None
                elif line.startswith("Quantity:"):
                    try:
                        record['quantity'] = int(line.replace("Quantity:", "").strip())
                    except ValueError:
                        print(f"Invalid quantity in file: {file_path}")
                        return None
        return record
    except (OSError, IOError) as e:
        print(f"Cannot open the file: {file_path}. Error: {str(e)}")
        return None


# Loop over all .txt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)
        record = parse_txt_file(file_path)
        if record is not None:
            data.append(record)
# Write parsed data to CSV
with open(output_file, mode='w', newline='') as csv_file:
    fieldnames = ['employee_id', 'unit_price', 'quantity']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f'Data successfully written to {output_file}')
