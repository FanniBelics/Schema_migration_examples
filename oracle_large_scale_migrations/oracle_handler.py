import oracledb
import os
from dotenv import load_dotenv
import re


load_dotenv()

conn = oracledb.connect(
    user=os.getenv("ORACLE_USERNAME"),
    password=os.getenv("ORACLE_PASSWORD"),
    host=os.getenv("HOST"),
    port=1521,
    service_name=os.getenv("SERVICE_NAME")
)

script_filepath = './oracle_large_scale_migrations/sql/'

def test_run():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dual")
    for row in cursor:
        print(row)
    cursor.close()
    
def split_sql_statements(sql_text):
    blocks = re.split(r"^\s*/\s*$", sql_text, flags=re.MULTILINE)
    statements = [b.strip() for b in blocks if b.strip()]
    return statements
    
def execute_sql_file(file_name):
    cursor = conn.cursor()
    try:
        with open(os.path.join(script_filepath, file_name), 'r') as file:
            sql_script = file.read()
        statements = split_sql_statements(sql_script)
        for statement in statements:
            cursor.execute(statement)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"Error occurred while executing {file_name}: {e}")
        raise
    finally:
        cursor.close()
        
def close_connection():
    conn.close()
    
if __name__ == "__main__":
    test_run()
    execute_sql_file('test_select.sql')
    close_connection()