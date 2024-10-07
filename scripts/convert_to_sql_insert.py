import csv
import sys

TABLE_NAME = "expenses"

FILE__CSV = "finance/receipts_from_last_night/mergedCSV.csv"

file_path = 'insert_expenses.sql'

data = []




def csv_to_sql_inserts(csv_file_path, table_name):
    try:
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            column_names = next(reader)
            for row in reader:
                columns = ', '.join(column_names)
                # for x in row:
                #     join = ', '.join("'" + str(x).replace("'", "''") + "'")
                # values = join
                employee = row[0].split()
                value = float(row[1])
                qunatity = int(row[2])
                insert_sql = (f'INSERT INTO {table_name} ({columns}) '
                              f'select employee_id, {value}, {qunatity} from employees where first_name = \'{employee[0]}\''
                              f' and last_name = \'{employee[1]}\';')
                data.append(insert_sql)

            with open(file_path, 'w') as output_file:
                output_file.write('USE memory.default;' + '\n')
                for line in data:
                    output_file.write(line + '\n')
    except Exception as e:
        print("Error while converting csv to sql inserts: ", e, file=sys.stderr)


csv_to_sql_inserts(FILE__CSV, TABLE_NAME)
print(f'Data successfully written to SQL definitions')
