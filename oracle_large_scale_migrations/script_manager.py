from oracle_handler import execute_sql_file
from time_manager import measure
from enums import states, json_tags
from recording_manager import record_step


def test_run(file_name: str):
    execute_sql_file(file_name)
    
def add_column_to_country():
    label = "expanding_country_table"
    
    
    # Insert data before migration
    print("Exec: insert_before_migration")
    with measure(label) as results_before_select:
        execute_sql_file("add_column/add_column_to_country_before_migration_insert.sql")
        
        results_before_select[json_tags.step_name.value] = 'add_column_before_migration_insert'
        results_before_select[json_tags.phase.value] = states.before_migration.value
        
    record_step(label, results_before_select)
    
    
    # Select data before migration
    print("Exec: select_before_migration")
    with measure(label) as results_before_select:
        execute_sql_file("add_column/add_column_to_country_before_migration_select.sql")
        
        results_before_select[json_tags.step_name.value] = 'add_column_before_migration_select'
        results_before_select[json_tags.phase.value] = states.before_migration.value
        
    record_step(label, results_before_select)
    
    
    # Update data before migration
    print("Exec: update_before_migration")
    with measure(label) as results_in_migration_update:
        execute_sql_file("add_column/add_column_to_country_migration_update.sql")
        
        results_in_migration_update[json_tags.step_name.value] = 'add_column_before_migration_update'
        results_in_migration_update[json_tags.phase.value] = states.before_migration.value
        
    record_step(label, results_in_migration_update)
    
    
    # Delete data before migration
    print("Exec: delete_before_migration")
    with measure(label) as results_before_migration_delete:
        execute_sql_file("add_column/add_column_to_country_migration_delete.sql")
        
        results_before_migration_delete[json_tags.step_name.value] = 'add_column_before_migration_delete'
        results_before_migration_delete[json_tags.phase.value] = states.before_migration.value
        
    record_step(label, results_before_migration_delete)
    
    print("Exec: re_insert")
    execute_sql_file("add_column/add_column_to_country_before_migration_insert.sql")

    # Migration steps: adding new column 
    print("Exec: migration")
    with measure(label) as results_in_migration_adding:
        execute_sql_file("add_column/add_column_to_country_in_migration_add_column.sql")
        
        results_in_migration_adding[json_tags.step_name.value] = 'add_column_in_migration_add_column'
        results_in_migration_adding[json_tags.phase.value] = states.in_migration_state.value
        
    record_step(label, results_in_migration_adding)
    
    # Fill new column with data    
    with measure(label) as results_in_migration_fill:
        execute_sql_file("add_column/add_column_to_country_in_migration_fill_columns.sql")
        
        results_in_migration_fill[json_tags.step_name.value] = 'add_column_in_migration_fill_columns'
        results_in_migration_fill[json_tags.phase.value] = states.in_migration_state.value
        
    record_step(label, results_in_migration_fill)
        
    # Insert data after migration
    print("Exec: insert_after_migration")
    with measure(label) as results_after_migration_insert:
        execute_sql_file("add_column/add_column_to_country_after_migration_insert.sql")
        
        results_after_migration_insert[json_tags.step_name.value] = 'add_column_after_migration_insert'
        results_after_migration_insert[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_insert)
    
    # Select data after migration
    print("Exec: select_after_migration")
    with measure(label) as results_after_migration_select:
        execute_sql_file("add_column/add_column_to_country_after_migration_select.sql")
        
        results_after_migration_select[json_tags.step_name.value] = 'add_column_after_migration_select'
        results_after_migration_select[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_select)
    
    # Update data after migration
    print("Exec: update_after_migration")
    with measure(label) as results_after_migration_update:
        execute_sql_file("add_column/add_column_to_country_migration_update.sql")
        
        results_after_migration_update[json_tags.step_name.value] = 'add_column_after_migration_update'
        results_after_migration_update[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_update)
    
    # Delete data after migration
    print("Exec: delete_after_migration")
    with measure(label) as results_after_migration_delete:
        execute_sql_file("add_column/add_column_to_country_migration_delete.sql")
        
        results_after_migration_delete[json_tags.step_name.value] = 'add_column_after_migration_delete'
        results_after_migration_delete[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_delete)
    
def merge_first_and_last_name_in_customer():
    label = "merging_first_and_last_name_in_customer"
    
    #Before migration measurements
    print("Exec: before migration select")
    with measure(label) as results_before_migration_select:
        execute_sql_file("merge_columns/merge_columns_migration_select.sql")
        
        results_before_migration_select[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_before_migration_select'
        results_before_migration_select[json_tags.phase.value] = states.before_migration.value
    
    record_step(label, results_before_migration_select)
    
    print("Exec: Before migration insert")
    with measure(label) as results_before_migration_insert:
        execute_sql_file("merge_columns/merge_columns_before_migration_insert.sql")
        
        results_before_migration_insert[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_before_migration_insert'
        results_before_migration_insert[json_tags.phase.value] = states.before_migration.value
    
    record_step(label, results_before_migration_insert)
    
    print("Exec: before migration update")
    with measure(label) as results_before_migration_update:
        execute_sql_file("merge_columns/merge_columns_migration_update.sql")
        
        results_before_migration_update[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_before_migration_update'
        results_before_migration_update[json_tags.phase.value] = states.before_migration.value

    record_step(label, results_before_migration_update)
    
    print("Exec: before migration delete")
    with measure(label) as results_before_migration_delete:
        execute_sql_file("merge_columns/merge_columns_migration_delete.sql")
        
        results_before_migration_delete[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_before_migration_delete'
        results_before_migration_delete[json_tags.phase.value] = states.before_migration.value

    record_step(label, results_before_migration_delete)
    
    #The actual migration steps
    print("Exec: migration")
    with measure(label) as results_in_migration:
        execute_sql_file("merge_columns/merge_columns_in_migration_migration.sql")
        
        results_in_migration[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_in_migration_migration'
        results_in_migration[json_tags.phase.value] = states.in_migration_state.value
    
    record_step(label, results_in_migration)
    
    #In migration measures: select, insert, update and delete 
    print("Exec: in migration select")
    with measure(label) as results_in_migration_select:
        execute_sql_file("merge_columns/merge_columns_migration_select.sql")
        
        results_in_migration_select[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_in_migration_select'
        results_in_migration_select[json_tags.phase.value] = states.in_migration_state.value

    record_step(label, results_in_migration_select)
    
    print("Exec: in migration insert")
    with measure(label) as results_in_migration_insert:
        execute_sql_file("merge_columns/merge_columns_in_migration_insert.sql")
        
        results_in_migration_insert[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_in_migration_insert'
        results_in_migration_insert[json_tags.phase.value] = states.in_migration_state.value

    record_step(label, results_in_migration_insert)
    
    print("Exec: in migration update")
    with measure(label) as results_in_migration_update:
        execute_sql_file("merge_columns/merge_columns_migration_update.sql")
        
        results_in_migration_update[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_in_migration_update'
        results_in_migration_update[json_tags.phase.value] = states.in_migration_state.value

    record_step(label, results_in_migration_update)

    print("Exec: in migration delete")
    with measure(label) as results_in_migration_delete:
        execute_sql_file("merge_columns/merge_columns_migration_delete.sql")
        
        results_in_migration_delete[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_in_migration_delete'
        results_in_migration_delete[json_tags.phase.value] = states.in_migration_state.value

    record_step(label, results_in_migration_delete)
    
    print("Exec: finishing migration state")
    with measure(label) as results_finishing_migration:
        execute_sql_file("merge_columns/merge_columns_after_migration_close_migration.sql")
        
        results_finishing_migration[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_finishing_migration'
        results_finishing_migration[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_finishing_migration)
    
    print("Exec: after migration select")
    with measure(label) as results_after_migration_select:
        execute_sql_file("merge_columns/merge_columns_migration_select.sql")
        
        results_after_migration_select[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_after_migration_select'
        results_after_migration_select[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_select)
    
    print("Exec: after migration insert")
    with measure(label) as results_after_migration_insert:
        execute_sql_file("merge_columns/merge_columns_after_migration_insert.sql")
        
        results_after_migration_insert[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_after_migration_insert'
        results_after_migration_insert[json_tags.phase.value] = states.after_migration.value

    record_step(label, results_after_migration_insert)
    
    print("Exec: after migration update")
    with measure(label) as results_after_migration_update:
        execute_sql_file("merge_columns/merge_columns_migration_update.sql")
        
        results_after_migration_update[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_after_migration_update'
        results_after_migration_update[json_tags.phase.value] = states.after_migration.value

    record_step(label, results_after_migration_update)
    
    print("Exec: after migration delete")
    with measure(label) as results_after_migration_delete:
        execute_sql_file("merge_columns/merge_columns_migration_delete.sql")
        
        results_after_migration_delete[json_tags.step_name.value] = 'merge_first_and_last_name_in_customer_after_migration_delete'
        results_after_migration_delete[json_tags.phase.value] = states.after_migration.value

    record_step(label, results_after_migration_delete)

def add_not_null_constraint_to_customer():
    label = "adding_not_null_constraint_to_customer"
    
    print("Exec: before migration select")
    with measure(label) as results_before_migration_select:
        execute_sql_file("add_constraint/add_constraint_migration_select.sql")
        
        results_before_migration_select[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_before_migration_select'
        results_before_migration_select[json_tags.phase.value] = states.before_migration.value
        
    record_step(label, results_before_migration_select)
    
    print("Exec: before migration insert")
    with measure(label) as results_before_migration_insert:
        execute_sql_file("add_constraint/add_constraint_before_migration_insert.sql")
        
        results_before_migration_insert[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_before_migration_insert'
        results_before_migration_insert[json_tags.phase.value] = states.before_migration.value

    record_step(label, results_before_migration_insert)
    
    print("Exec: before migration update")
    with measure(label) as results_before_migration_update:
        execute_sql_file("add_constraint/add_constraint_migration_update.sql")
        
        results_before_migration_update[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_before_migration_update'
        results_before_migration_update[json_tags.phase.value] = states.before_migration.value

    record_step(label, results_before_migration_update)
    
    print("Exec: before migration delete")
    with measure(label) as results_before_migration_delete:
        execute_sql_file("add_constraint/add_constraint_migration_delete.sql")
        
        results_before_migration_delete[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_before_migration_delete'
        results_before_migration_delete[json_tags.phase.value] = states.before_migration.value
    
    record_step(label, results_before_migration_delete)
    
    print("Exec: migration")
    with measure(label) as results_in_migration:
        execute_sql_file("add_constraint/add_constraint_in_migration_migration.sql")
        
        results_in_migration[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_in_migration_add_constraint'
        results_in_migration[json_tags.phase.value] = states.in_migration_state.value
        
    record_step(label, results_in_migration)
    
    print("Exec: in migration select")
    with measure(label) as results_in_migration_select:
        execute_sql_file("add_constraint/add_constraint_migration_select.sql")
        
        results_in_migration_select[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_in_migration_select'
        results_in_migration_select[json_tags.phase.value] = states.in_migration_state.value
    
    record_step(label, results_in_migration_select)
    
    print("Exec: in migration insert")
    with measure(label) as results_in_migration_insert:
        execute_sql_file("add_constraint/add_constraint_in_migration_insert.sql")
        
        results_in_migration_insert[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_in_migration_insert'
        results_in_migration_insert[json_tags.phase.value] = states.in_migration_state.value
        
    record_step(label, results_in_migration_insert)
    
    print("Exec: in migration update")
    with measure(label) as results_in_migration_update:
        execute_sql_file("add_constraint/add_constraint_migration_update.sql")
        
        results_in_migration_update[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_in_migration_update'
        results_in_migration_update[json_tags.phase.value] = states.in_migration_state.value

    record_step(label, results_in_migration_update)
    
    print("Exec: in migration delete")
    with measure(label) as results_in_migration_delete:
        execute_sql_file("add_constraint/add_constraint_migration_delete.sql")
        
        results_in_migration_delete[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_in_migration_delete'
        results_in_migration_delete[json_tags.phase.value] = states.in_migration_state.value

    record_step(label, results_in_migration_delete)
    
    print("Exec: after migration close migration")
    with measure(label) as results_after_migration_close_migration:
        execute_sql_file("add_constraint/add_constraint_after_migration_close_migration.sql")
        
        results_after_migration_close_migration[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_after_migration_close_migration'
        results_after_migration_close_migration[json_tags.phase.value] = states.after_migration.value

    record_step(label, results_after_migration_close_migration)
    
    print("Exec: after migration select")
    with measure(label) as results_after_migration_select:
        execute_sql_file("add_constraint/add_constraint_migration_select.sql")
        
        results_after_migration_select[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_after_migration_select'
        results_after_migration_select[json_tags.phase.value] = states.after_migration.value

    record_step(label, results_after_migration_select)
    
    print("Exec: after migration insert")
    with measure(label) as results_after_migration_insert:
        execute_sql_file("add_constraint/add_constraint_after_migration_insert.sql")
        
        results_after_migration_insert[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_after_migration_insert'
        results_after_migration_insert[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_insert)
    
    print("Exec: after migration update")
    with measure(label) as results_after_migration_update:
        execute_sql_file("add_constraint/add_constraint_migration_update.sql")
        
        results_after_migration_update[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_after_migration_update'
        results_after_migration_update[json_tags.phase.value] = states.after_migration.value

    record_step(label, results_after_migration_update)
    
    print("Exec: after migration delete")
    with measure(label) as results_after_migration_delete:
        execute_sql_file("add_constraint/add_constraint_migration_delete.sql")
        
        results_after_migration_delete[json_tags.step_name.value] = 'add_not_null_constraint_to_customer_after_migration_delete'
        results_after_migration_delete[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_delete)

def remove_not_null_constraint_from_customer():
    label = "removing_not_null_constraint_from_customer"
    
    # print("Exec: before migration select")
    # with measure(label) as results_before_migration_select:
    #     execute_sql_file("remove_constraint/remove_constraint_migration_select.sql")
        
    #     results_before_migration_select[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_before_migration_select'
    #     results_before_migration_select[json_tags.phase.value] = states.before_migration.value
        
    # record_step(label, results_before_migration_select)
    
    # print("Exec: before migration insert")
    # with measure(label) as results_before_migration_insert:
    #     execute_sql_file("remove_constraint/remove_constraint_before_migration_insert.sql")
        
    #     results_before_migration_insert[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_before_migration_insert'
    #     results_before_migration_insert[json_tags.phase.value] = states.before_migration.value
        
    # record_step(label, results_before_migration_insert)
    
    # print("Exec: before migration update")
    # with measure(label) as results_before_migration_update:
    #     execute_sql_file("remove_constraint/remove_constraint_migration_update.sql")
        
    #     results_before_migration_update[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_before_migration_update'
    #     results_before_migration_update[json_tags.phase.value] = states.before_migration.value
        
    # record_step(label, results_before_migration_update)
    
    # print("Exec: before migration delete")
    # with measure(label) as results_before_migration_delete:
    #     execute_sql_file("remove_constraint/remove_constraint_migration_delete.sql")
        
    #     results_before_migration_delete[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_before_migration_delete'
    #     results_before_migration_delete[json_tags.phase.value] = states.before_migration.value
        
    # record_step(label, results_before_migration_delete)
    
    # print("Exec: migration")
    # with measure(label) as results_migration:
    #     execute_sql_file("remove_constraint/remove_constraint_in_migration_migration.sql")
        
    #     results_migration[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_migration'
    #     results_migration[json_tags.phase.value] = states.in_migration_state.value
        
    # record_step(label, results_migration) 
    
    # print("Exec: in migration select")
    # with measure(label) as results_in_migration_select:
    #     execute_sql_file("remove_constraint/remove_constraint_migration_select.sql")
        
    #     results_in_migration_select[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_in_migration_select'
    #     results_in_migration_select[json_tags.phase.value] = states.in_migration_state.value
        
    # record_step(label, results_in_migration_select)
    
    # print("Exec: in migration insert")
    # with measure(label) as results_in_migration_insert:
    #     execute_sql_file("remove_constraint/remove_constraint_in_migration_insert.sql")
        
    #     results_in_migration_insert[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_in_migration_insert'
    #     results_in_migration_insert[json_tags.phase.value] = states.in_migration_state.value
        
    # record_step(label, results_in_migration_insert)
    
    # print("Exec: in migration update")
    # with measure(label) as results_in_migration_update:
    #     execute_sql_file("remove_constraint/remove_constraint_migration_update.sql")
        
    #     results_in_migration_update[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_in_migration_update'
    #     results_in_migration_update[json_tags.phase.value] = states.in_migration_state.value
        
    # record_step(label, results_in_migration_update)
    
    # print("Exec: in migration delete")
    # with measure(label) as results_in_migration_delete:
    #     execute_sql_file("remove_constraint/remove_constraint_migration_delete.sql")
        
    #     results_in_migration_delete[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_in_migration_delete'
    #     results_in_migration_delete[json_tags.phase.value] = states.in_migration_state.value
        
    # record_step(label, results_in_migration_delete)
    
    # print("Exec: closing migration")
    # with measure(label) as results_after_migration_close_migration:
    #     execute_sql_file("remove_constraint/remove_constraint_after_migration_close_migration.sql")
        
    #     results_after_migration_close_migration[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_after_migration_close_migration'
    #     results_after_migration_close_migration[json_tags.phase.value] = states.after_migration.value

    # record_step(label, results_after_migration_close_migration)
    
    # print("Exec: after migration select")
    # with measure(label) as results_after_migration_select:
    #     execute_sql_file("remove_constraint/remove_constraint_migration_select.sql")
        
    #     results_after_migration_select[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_after_migration_select'
    #     results_after_migration_select[json_tags.phase.value] = states.after_migration.value
        
    # record_step(label, results_after_migration_select)
    
    print("Exec: after migration insert")
    with measure(label) as results_after_migration_insert:
        execute_sql_file("remove_constraint/remove_constraint_after_migration_insert.sql")
        
        results_after_migration_insert[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_after_migration_insert'
        results_after_migration_insert[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_insert)
    
    print("Exec: after migration update")
    with measure(label) as results_after_migration_update:
        execute_sql_file("remove_constraint/remove_constraint_migration_update.sql")
        
        results_after_migration_update[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_after_migration_update'
        results_after_migration_update[json_tags.phase.value] = states.after_migration.value

    record_step(label, results_after_migration_update)

    print("Exec: after migration delete")
    with measure(label) as results_after_migration_delete:
        execute_sql_file("remove_constraint/remove_constraint_migration_delete.sql")
        
        results_after_migration_delete[json_tags.step_name.value] = 'remove_not_null_constraint_from_customer_after_migration_delete'
        results_after_migration_delete[json_tags.phase.value] = states.after_migration.value
        
    record_step(label, results_after_migration_delete)

if __name__ == "__main__":
    # with measure("test_run") as results:
    #     test_run("test_select.sql")
    
    #     results[json_tags.step_name.value] = 'test_run'
    #     results[json_tags.phase.value] = states.before_migration.value
        
    # print(results)
    # record_step("test_additional_migration", results)
    
    #add_column_to_country()
    #merge_first_and_last_name_in_customer()
    #add_not_null_constraint_to_customer()
    remove_not_null_constraint_from_customer()