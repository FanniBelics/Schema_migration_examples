def generate_inserts_before_migration(element_range: int, threshold: int):
    with open("add_column_to_country_before_migration_insert.sql", "w") as f:
        for i in range(element_range):
            i = i + threshold
            f.write(f"INSERT INTO sh.countries (COUNTRY_ID, COUNTRY_ISO_CODE, COUNTRY_NAME, COUNTRY_SUBREGION, COUNTRY_SUBREGION_ID,\
                    COUNTRY_REGION, COUNTRY_REGION_ID, COUNTRY_TOTAL, COUNTRY_TOTAL_ID, COUNTRY_NAME_HIST)\
                    VALUES ({i}, '{chr(65 + (i % 26))+chr(65 + ((i+1) % 26))}', 'Country_{i}', 'Subregion_{i%5 + 1 }',\
                    {i%5 + 1}, 'Western Europe', 52799, 'World total', 52806, NULL)\n/\n".replace("                    ", " "))
            
        f.write("COMMIT\n/\n")
            
def generate_updates(element_range: int, threshold: int):
    with open("add_column_to_country_migration_update.sql", "w") as f:
        for i in range(element_range):
            i = i + threshold
            f.write(f"UPDATE sh.countries SET COUNTRY_NAME = COUNTRY_NAME || '_test' WHERE COUNTRY_ID = {i}\n/\n")
            
        f.write("COMMIT\n/\n")
        
def generate_inserts_after_migration(element_range: int, threshold: int):
    with open("add_column_to_country_after_migration_insert.sql", "w") as f:
        for i in range(element_range):
            i = i + threshold + element_range
            f.write(f"INSERT INTO sh.countries (COUNTRY_ID, COUNTRY_ISO_CODE, COUNTRY_NAME, COUNTRY_SUBREGION, COUNTRY_SUBREGION_ID,\
                    COUNTRY_REGION, COUNTRY_REGION_ID, COUNTRY_TOTAL, COUNTRY_TOTAL_ID, COUNTRY_NAME_HIST, COUNTRY_ISO_CODE_3)\
                    VALUES ({i}, '{chr(65 + (i % 26))+chr(65 + ((i+1) % 26))}', 'Country_{i}', 'Subregion_{i%5 + 1 }',\
                    {i%5 + 1}, 'Western Europe', 52799, 'World total', 52806, NULL, '{chr(65 + (i % 26))+chr(65 + ((i+1) % 26))+chr(65 + ((i+2) % 26))}')\n/\n".replace("                    ", " "))
        
        f.write("COMMIT\n/\n")
        
def generate_delete(element_range: int, threshold: int):
    with open("add_column_to_country_migration_delete.sql", "w") as f:
        for i in range(element_range):
            i = i + threshold
            f.write(f"DELETE FROM sh.countries WHERE COUNTRY_ID = {i}\n/\n")
            
        f.write("COMMIT\n/\n")

if __name__ == "__main__":
    n = 10000
    threshold = 53000
    generate_inserts_before_migration(n, threshold)
    generate_updates(n, threshold)
    generate_inserts_after_migration(n, threshold)
    generate_delete(n, threshold)