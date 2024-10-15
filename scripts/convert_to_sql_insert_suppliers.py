"""
Module for converting data from suppliers csv file to sql formatted statements.
Creates SQL files for later execution on Trino
"""
import csv
import sys

TABLE_NAME = "supplier"

FILE__CSV = "../finance/invoices_due/mergedCSVcompanies.csv"

file_path = '../insert_suppliers.sql'

data = []


def csv_suppliers_to_sql_inserts(csv_file_path, table_name):
    """
    converts parsed data from csv files into sql statement and writes data into output sql srcipt files
    Parsed data: Suppliers
    """
    try:
        with (open(csv_file_path, 'r') as csv_file):
            reader = csv.reader(csv_file)
            column_names = next(reader)
            id_ = 0
            data_ = []

            for row in reader:
                data_.append(row[1])
            data_.sort()
            data_ = list(dict.fromkeys(data_))
            for row in data_:
                columns = ', '.join(column_names)
                id_ += 1
                name = row.replace("'","''")
                insert_sql = (f'INSERT INTO {table_name} ({columns}) '
                              f'values ('
                              f'{id_},'
                              f' \'{name}\');'
                              ).replace("'", "\'")
                data.append(insert_sql)

            data.sort()
            with open(file_path, 'w') as output_file:
                output_file.write('USE memory.default;' + '\n')
                for line in set(data):
                    output_file.write(line + '\n')
    except Exception as e:
        print("Error while converting csv to sql inserts: ", e, file=sys.stderr)


csv_suppliers_to_sql_inserts(FILE__CSV, TABLE_NAME)
print(f'Data successfully written to SQL definitions')
