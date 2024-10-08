import csv
import sys

import dateparser

TABLE_NAME = "invoice"

FILE__CSV = "../finance/invoices_due/mergedCSV.csv"

file_path = '../insert_invoices.sql'

data = []


def csv_to_sql_inserts(csv_file_path, table_name):
    try:
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            column_names = next(reader)
            id = 0
            for row in reader:
                id += 1
                columns = ', '.join(column_names)
                company_name = row[4].replace("'", "''")       # yuck!
                invoice_amount = float(row[2])                              # bleh
                due_date = dateparser.parse(row[3]).strftime('%Y-%m-%d')    # ugh
                insert_sql = (f'INSERT INTO {table_name} ({columns.replace(", name", "")}) '
                              f'select supplier.id, '
                              f'{id},'
                              f'{invoice_amount}, '
                              f'CAST(\'{due_date}\' AS DATE) '
                              f'from supplier where name = \'{company_name}\';')
                data.append(insert_sql)

            with open(file_path, 'w') as output_file:
                output_file.write('USE memory.default;' + '\n')
                for line in data:
                    output_file.write(line + '\n')
    except Exception as e:
        print("Error while converting csv to sql inserts: ", e, file=sys.stderr)


csv_to_sql_inserts(FILE__CSV, TABLE_NAME)
print(f'Data successfully written to SQL definitions')
