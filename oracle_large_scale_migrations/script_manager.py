from oracle_handler import execute_sql_file
from time_manager import measure
from enums import states, json_tags


def test_run(file_name: str):
    execute_sql_file(file_name)

if __name__ == "__main__":
    with measure("test_run") as result:
        test_run("test_select.sql")
    
        result[json_tags.step_name.value] = 'test_run'
        result[json_tags.phase.value] = states.before_migration.value
        
    print(result)