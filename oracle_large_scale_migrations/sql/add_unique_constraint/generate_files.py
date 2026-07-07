from faker import Faker
from faker.providers import DynamicProvider
from faker_ecommerce import EcommerceProvider
import random 

faker = Faker()
faker.add_provider(EcommerceProvider)

def generate_inserts_before_migration(element_range: int, threshold: int = 200):
    with open("add_unique_before_migration_insert.sql", "w") as f:
        for i in range(1, element_range + 1):
            i = i + threshold
            f.write(f"INSERT INTO SH.PRODUCTS(PROD_ID, PROD_NAME, PROD_DESC, PROD_SUBCATEGORY,\
                    PROD_SUBCATEGORY_ID, PROD_SUBCATEGORY_DESC, PROD_CATEGORY, PROD_CATEGORY_ID,\
                    PROD_CATEGORY_DESC, PROD_WEIGHT_CLASS, PROD_UNIT_OF_MEASURE, PROD_PACK_SIZE, SUPPLIER_ID,\
                    PROD_STATUS, PROD_LIST_PRICE, PROD_MIN_PRICE, PROD_TOTAL, PROD_TOTAL_ID, PROD_SRC_ID,\
                    PROD_EFF_FROM, PROD_EFF_TO, PROD_VALID)\
                VALUES({i}, \'{faker.product_name()}\', \'{faker.product_description()}\', \'{faker.product_category()}\',\
                        {2044}, \'{faker.product_description()}\', \'{faker.product_category()}\', {204},\
                           \'{faker.product_description()}\', {1}, \'{'U'}\', \'{'P'}\', \'{1}\',\
                            \'STATUS\', {faker.random_number(digits=2)}, {faker.random_number(digits=2)}, \'TOTAL\', 1, NULL,\
                            TO_DATE(\'{faker.date_time_between(start_date='-5y', end_date='now')}\', \'YYYY-MM-DD HH24:MI:SS\'), NULL, \'A\')\n/\n".replace("             ", " "))
            
        f.write("COMMIT\n/\n")
        
def generate_inserts_after_migration(element_range: int, threshold: int = 200):
    with open("add_unique_after_migration_insert.sql", "w") as f:
        for i in range(1, element_range + 1):
            i = i + threshold
            f.write(f"INSERT INTO SH.PRODUCTS(PROD_ID, PROD_NAME, PROD_DESC, PROD_SUBCATEGORY,\
                    PROD_SUBCATEGORY_ID, PROD_SUBCATEGORY_DESC, PROD_CATEGORY, PROD_CATEGORY_ID,\
                    PROD_CATEGORY_DESC, PROD_WEIGHT_CLASS, PROD_UNIT_OF_MEASURE, PROD_PACK_SIZE, SUPPLIER_ID,\
                    PROD_STATUS, PROD_LIST_PRICE, PROD_MIN_PRICE, PROD_TOTAL, PROD_TOTAL_ID, PROD_SRC_ID,\
                    PROD_EFF_FROM, PROD_EFF_TO, PROD_VALID)\
                VALUES({i}, \'{faker.product_name()+'_'+str(i)}\', \'{faker.product_description()}\', \'{faker.product_category()}\',\
                        {2044}, \'{faker.product_description()}\', \'{faker.product_category()}\', {204},\
                           \'{faker.product_description()}\', {1}, \'{'U'}\', \'{'P'}\', \'{1}\',\
                            \'STATUS\', {faker.random_number(digits=2)}, {faker.random_number(digits=2)}, \'TOTAL\', 1, NULL,\
                                TO_DATE(\'{faker.date_time_between(start_date='-5y', end_date='now')}\', \'YYYY-MM-DD HH24:MI:SS\'), NULL, \'A\')\n/\n".replace("             ", " "))
            
        f.write("COMMIT\n/\n")
        
def generate_inserts_in_migration(element_range: int, threshold: int = 200):
    with open("add_unique_in_migration_insert.sql", "w") as f:
        for i in range(1, element_range + 1):
            i = i + threshold
            if(random.randint(0, 1) == 0):
                #Schema version 1
                f.write(f"INSERT INTO SH.PRODUCTS(PROD_ID, PROD_NAME, PROD_DESC, PROD_SUBCATEGORY,\
                    PROD_SUBCATEGORY_ID, PROD_SUBCATEGORY_DESC, PROD_CATEGORY, PROD_CATEGORY_ID,\
                    PROD_CATEGORY_DESC, PROD_WEIGHT_CLASS, PROD_UNIT_OF_MEASURE, PROD_PACK_SIZE, SUPPLIER_ID,\
                    PROD_STATUS, PROD_LIST_PRICE, PROD_MIN_PRICE, PROD_TOTAL, PROD_TOTAL_ID, PROD_SRC_ID,\
                    PROD_EFF_FROM, PROD_EFF_TO, PROD_VALID, SCHEMA_VERSION)\
                VALUES({i}, \'{faker.product_name()}\', \'{faker.product_description()}\', \'{faker.product_category()}\',\
                        {2044}, \'{faker.product_description()}\', \'{faker.product_category()}\', {204},\
                           \'{faker.product_description()}\', {1}, \'{'U'}\', \'{'P'}\', \'{1}\',\
                            \'STATUS\', {faker.random_number(digits=2)}, {faker.random_number(digits=2)}, \'TOTAL\', 1, NULL,\
                                TO_DATE(\'{faker.date_time_between(start_date='-5y', end_date='now')}\', \'YYYY-MM-DD HH24:MI:SS\'), NULL, \'A\', 1)\n/\n".replace("             ", " "))
            else:
                #Schema version 2
                f.write(f"INSERT INTO SH.PRODUCTS(PROD_ID, PROD_NAME, PROD_DESC, PROD_SUBCATEGORY,\
                    PROD_SUBCATEGORY_ID, PROD_SUBCATEGORY_DESC, PROD_CATEGORY, PROD_CATEGORY_ID,\
                    PROD_CATEGORY_DESC, PROD_WEIGHT_CLASS, PROD_UNIT_OF_MEASURE, PROD_PACK_SIZE, SUPPLIER_ID,\
                    PROD_STATUS, PROD_LIST_PRICE, PROD_MIN_PRICE, PROD_TOTAL, PROD_TOTAL_ID, PROD_SRC_ID,\
                    PROD_EFF_FROM, PROD_EFF_TO, PROD_VALID, SCHEMA_VERSION)\
                VALUES({i}, \'{faker.product_name()+'_'+str(i)}\', \'{faker.product_description()}\', \'{faker.product_category()}\',\
                        {2044}, \'{faker.product_description()}\', \'{faker.product_category()}\', {204},\
                           \'{faker.product_description()}\', {1}, \'{'U'}\', \'{'P'}\', \'{1}\',\
                            \'STATUS\', {faker.random_number(digits=2)}, {faker.random_number(digits=2)}, \'TOTAL\', 1, NULL,\
                                TO_DATE(\'{faker.date_time_between(start_date='-5y', end_date='now')}\', \'YYYY-MM-DD HH24:MI:SS\'), NULL, \'A\', 2)\n/\n".replace("             ", " "))
            
        f.write("COMMIT\n/\n")
        
def generate_updates(element_range: int, threshold: int = 200):
    with open("add_unique_migration_update.sql", "w") as f:
        for i in range(1, element_range + 1):
            i = i + threshold
            f.write(f"UPDATE SH.PRODUCTS SET PROD_DESC = \'{faker.product_description()}\' WHERE PROD_ID = {i}\n/\n")
        f.write("COMMIT\n/\n")
        
def generate_deletes(element_range: int, threshold: int = 200):
    with open("add_unique_migration_delete.sql", "w") as f:
        for i in range(1, element_range + 1):
            i = i + threshold
            f.write(f"DELETE FROM SH.PRODUCTS WHERE PROD_ID = {i}\n/\n")
        f.write("COMMIT\n/\n")

if __name__ == "__main__":
    n = 10000
    generate_inserts_before_migration(n)
    generate_inserts_after_migration(n)
    generate_inserts_in_migration(n)
    #generate_updates(n)
    #generate_deletes(n)

