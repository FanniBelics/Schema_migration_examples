from oracle_handler import execute_sql_file
from time_manager import measure
from enums import states, json_tags
from recording_manager import record_step


def test_run(file_name: str):
    execute_sql_file(file_name)

if __name__ == "__main__":
    with measure("test_run") as results:
        test_run("test_select.sql")
    
        results[json_tags.step_name.value] = 'test_run'
        results[json_tags.phase.value] = states.before_migration.value
        
    print(results)
    record_step("test_additional_migration", results)