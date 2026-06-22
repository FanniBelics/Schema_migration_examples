from oracle_handler import execute_sql_file
from time_manager import measure
from enums import states, json_tags
from recording_manager import record_step


def test_run(file_name: str):
    execute_sql_file(file_name)
    
def add_column_to_country():
    label = "expanding_country_table"
    with measure(label) as results_before_select:
        execute_sql_file("add_column_to_country_before_migration_select.sql")
        
        results_before_select[json_tags.step_name.value] = 'add_column_before_select'
        results_before_select[json_tags.phase.value] = states.before_migration.value
        
    record_step(label, results_before_select)
        
    with measure(label) as results_in_migration_adding:
        execute_sql_file("add_column_to_country_in_migration_add_column.sql")
        
        results_in_migration_adding[json_tags.step_name.value] = 'add_column_in_migration_add_column'
        results_in_migration_adding[json_tags.phase.value] = states.in_migration_state.value
        
    record_step(label, results_in_migration_adding)
        
    with measure(label) as results_in_migration_fill:
        execute_sql_file("add_column_to_country_in_migration_fill_columns.sql")
        
        results_in_migration_fill[json_tags.step_name.value] = 'add_column_in_migration_fill_columns'
        results_in_migration_fill[json_tags.phase.value] = states.in_migration_state.value
        
    record_step(label, results_in_migration_fill)
        
    with measure(label) as results_after_migration_adding:
        execute_sql_file("add_column_to_country_after_migration_select.sql")
        
        results_after_migration_adding[json_tags.step_name.value] = 'add_column_after_migration_select'
        results_after_migration_adding[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_adding)

if __name__ == "__main__":
    # with measure("test_run") as results:
    #     test_run("test_select.sql")
    
    #     results[json_tags.step_name.value] = 'test_run'
    #     results[json_tags.phase.value] = states.before_migration.value
        
    # print(results)
    # record_step("test_additional_migration", results)
    
    add_column_to_country()