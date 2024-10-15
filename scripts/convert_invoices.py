#  Copyright (c) 2024.
"""
Module for converting data from invoicses text files to csv format file for easier handling.
It merges data from txt files in a given input folder into a single csv file.
"""
import csv
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

input_folder = "../finance/invoices_due"
output_file = "../finance/invoices_due/mergedCSV.csv"
output_file2 = "../finance/invoices_due/mergedCSVcompanies.csv"

data = []


def parse_invoices_txt_files(file_path):
    """
    Parses invoices files for a given filepath

    :type file_path: str
    """
    record = {}

    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("Company Name:"):
                    record['name'] = (line.replace("Company Name:", "").strip())
                elif line.startswith("Invoice Amount:"):
                    try:
                        record['invoice_amount'] = float(line.replace("Invoice Amount:", "").strip())
                    except ValueError:
                        print(f"Invalid price in file: {file_path}")
                        return None
                elif line.startswith("Due Date:"):
                    try:
                        current_date = datetime.now()
                        new_date = current_date + relativedelta(months=int(line.replace("Due Date:", "").strip()[0]))

                        record['due_date'] = new_date
                    except ValueError:
                        print(f"Invalid quantity in file: {file_path}")
                        return None
                record['id'] = 0
                record['supplier_id'] = 0
        return record
    except (OSError, IOError) as e:
        print(f"Cannot open the file: {file_path}. Error: {str(e)}")
        return None


# files in input folder loop
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)
        record = parse_invoices_txt_files(file_path)
        if record is not None and record not in data:
            data.append(record)
# write data to output files. first files with invoices and in second step files with company names
# step 1:
with open(output_file, mode='w', newline='') as csv_file:
    fieldnames = ['supplier_id', 'id', 'invoice_amount', 'due_date', 'name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)
# step 2:
with open(output_file2, mode='w', newline='') as csv_file:
    fieldnames = ['id', 'name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        row.pop('invoice_amount')
        row.pop('due_date')
        row.pop('supplier_id')
        writer.writerow(row)

print(f'Data successfully written to {output_file}')
