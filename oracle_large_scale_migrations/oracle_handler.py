import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

conn = oracledb.connect(
    user=os.getenv("ORACLE_USERNAME"),
    password=os.getenv("ORACLE_PASSWORD"),
    host=os.getenv("HOST"),
    port=1521,
    service_name=os.getenv("SERVICE_NAME")
)

script_filepath = './sql/'

def test_run():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dual")
    for row in cursor:
        print(row)
    cursor.close()
    
def execute_sql_file(file_name):
    try:
        with open(os.path.join(script_filepath, file_name), 'r') as file:
            sql_script = file.read()
        cursor = conn.cursor()
        cursor.execute(sql_script)
        cursor.close()
    except Exception as e:
        print(f"Error occurred while executing {file_name}: {e}")
    
if __name__ == "__main__":
    test_run()
    execute_sql_file('test_select.sql')