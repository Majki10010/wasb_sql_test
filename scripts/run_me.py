import os
import subprocess
import sys


def execute_script(script_name):
    # Construct the full path to the script
    script_path = os.path.join('scripts/', f"{script_name}.py")
    # Check if the script exists in the designated folder
    if not os.path.isfile(script_path):
        print(f"Error: {script_name}.py not foun")
        return

    # Execute the script using subprocess
    try:
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        print(f"Output of {script_name}.py:\n{result.stdout}")
        if result.stderr:
            print(f"Errors:\n{result.stderr}")
    except Exception as e:
        print(f"Failed to execute {script_name}.py: {str(e)}")


if __name__ == "__main__":
    execute_script('convert_expenses')
    execute_script('convert_to_sql_insert')
