from faker import Faker
from faker.providers import DynamicProvider
import random 

faker = Faker(["en_US", "en_GB"])

countries_provider = DynamicProvider(
    provider_name="countries",
    elements=[52790, 52776, 52789, 52784, 52780, 52777, 52779, 52778, 52788, 52786, 52775, 52773, 52783, 52782, 52781, 52774, 52785, 52791, 52787, 52772, 52771, 52769, 52770]
)

income_provider = DynamicProvider(
    provider_name="income_levels",
    elements=["C: 50,000 - 69,999", "F: 110,000 - 129,999", "I: 170,000 - 189,999", "H: 150,000 - 169,999"]
)

def generate_after_migration_inserts(element_range: int, threshold: int = 104500):
    with open("wrap_customer_contact_after_migration_insert.sql", "w") as f:
        for i in range(1, element_range + 1):
            i = i + threshold
            f.write(f"INSERT INTO SH.CUSTOMERS(CUST_ID, CUST_FULL_NAME,\
                CUST_GENDER, CUST_YEAR_OF_BIRTH, CUST_MARITAL_STATUS, CUST_STREET_ADDRESS,\
                CUST_POSTAL_CODE, CUST_CITY, CUST_CITY_ID, CUST_STATE_PROVINCE, CUST_STATE_PROVINCE_ID,\
                COUNTRY_ID, CUST_INCOME_LEVEL, CUST_CREDIT_LIMIT,\
                CUST_TOTAL, CUST_TOTAL_ID, CUST_SRC_ID, CUST_EFF_FROM, CUST_EFF_TO, CUST_VALID, CUSTOMER_CONTACT)\
                VALUES ({i}, \'{faker.first_name() + " " + faker.last_name().replace("'", " ")}\', {faker.random_element(elements=('\'M\'', '\'F\'', 'NULL'))},\
                {faker.year()}, \'{faker.random_element(elements=('single', 'married', 'divorced', 'unknown'))}\', \
                \'{faker.street_address().replace('\n', ' ').replace("'", " ")}\', {faker.postalcode()}, \'{faker.city().replace("'", " ")}\', {faker.random_int(min=1, max=1000)},\
                \'{faker.state()}\', {faker.random_int(min=1, max=1000)}, \'{faker.random_element(elements=countries_provider.elements)}\', \
                \'{faker.random_element(elements=income_provider.elements)}\', {faker.random_int(min=1, max=100000)}, \
                \'Customer total\', \'52772\', NULL, to_date(\'{faker.date_time_between(start_date='-5y', end_date='now')}\', \'YYYY-MM-DD HH24:MI:SS\'), to_date(\'{faker.date_time_between(start_date='now', end_date='+5y')}\', \'YYYY-MM-DD HH24:MI:SS\'), \
                \'{faker.random_element(elements=('A', 'I'))}\',\
                customer_contact_type(\'{faker.phone_number()}\', \'{faker.email()}\'))\n/\n".replace("                ", " "))
        
        f.write("COMMIT\n/\n")
                

def generate_in_migration_inserts(element_range: int, threshold: int = 104500):
    with open("wrap_customer_contact_in_migration_insert.sql", "w") as f:
        for i in range(1, element_range + 1):
            i = i + threshold
            if(random.randint(0, 1) == 0):
                # Schema version 1
                f.write(f"INSERT INTO SH.CUSTOMERS(CUST_ID, CUST_FULL_NAME,\
                CUST_GENDER, CUST_YEAR_OF_BIRTH, CUST_MARITAL_STATUS, CUST_STREET_ADDRESS,\
                CUST_POSTAL_CODE, CUST_CITY, CUST_CITY_ID, CUST_STATE_PROVINCE, CUST_STATE_PROVINCE_ID,\
                COUNTRY_ID, CUST_MAIN_PHONE_NUMBER, CUST_INCOME_LEVEL, CUST_CREDIT_LIMIT, CUST_EMAIL,\
                CUST_TOTAL, CUST_TOTAL_ID, CUST_SRC_ID, CUST_EFF_FROM, CUST_EFF_TO, CUST_VALID, SCHEMA_VERSION)\
                VALUES ({i}, \'{faker.first_name() + " " + faker.last_name().replace("'", " ")}\', {faker.random_element(elements=('\'M\'', '\'F\'', 'NULL'))},\
                {faker.year()}, \'{faker.random_element(elements=('single', 'married', 'divorced', 'unknown'))}\', \
                \'{faker.street_address().replace('\n', ' ').replace("'", " ")}\', {faker.postalcode()}, \'{faker.city().replace("'", " ")}\', {faker.random_int(min=1, max=1000)},\
                \'{faker.state()}\', {faker.random_int(min=1, max=1000)}, \'{faker.random_element(elements=countries_provider.elements)}\', \
                \'{faker.phone_number()}\', \'{faker.random_element(elements=income_provider.elements)}\', {faker.random_int(min=1, max=100000)}, \
                \'{faker.email()}\', \'Customer total\', \'52772\', NULL, to_date(\'{faker.date_time_between(start_date='-5y', end_date='now')}\', \'YYYY-MM-DD HH24:MI:SS\'), to_date(\'{faker.date_time_between(start_date='now', end_date='+5y')}\', \'YYYY-MM-DD HH24:MI:SS\'), \
                \'{faker.random_element(elements=('A', 'I'))}\', 1)\n/\n".replace("                ", " "))
            else:
                # Schema version 2
                f.write(f"INSERT INTO SH.CUSTOMERS(CUST_ID, CUST_FULL_NAME,\
                CUST_GENDER, CUST_YEAR_OF_BIRTH, CUST_MARITAL_STATUS, CUST_STREET_ADDRESS,\
                CUST_POSTAL_CODE, CUST_CITY, CUST_CITY_ID, CUST_STATE_PROVINCE, CUST_STATE_PROVINCE_ID,\
                COUNTRY_ID, CUST_INCOME_LEVEL, CUST_CREDIT_LIMIT,\
                CUST_TOTAL, CUST_TOTAL_ID, CUST_SRC_ID, CUST_EFF_FROM, CUST_EFF_TO, CUST_VALID, CUSTOMER_CONTACT, SCHEMA_VERSION)\
                VALUES ({i}, \'{faker.first_name() + " " + faker.last_name().replace("'", " ")}\', {faker.random_element(elements=('\'M\'', '\'F\'', 'NULL'))},\
                {faker.year()}, \'{faker.random_element(elements=('single', 'married', 'divorced', 'unknown'))}\', \
                \'{faker.street_address().replace('\n', ' ').replace("'", " ")}\', {faker.postalcode()}, \'{faker.city().replace("'", " ")}\', {faker.random_int(min=1, max=1000)},\
                \'{faker.state()}\', {faker.random_int(min=1, max=1000)}, \'{faker.random_element(elements=countries_provider.elements)}\', \
                \'{faker.random_element(elements=income_provider.elements)}\', {faker.random_int(min=1, max=100000)}, \
                \'Customer total\', \'52772\', NULL, to_date(\'{faker.date_time_between(start_date='-5y', end_date='now')}\', \'YYYY-MM-DD HH24:MI:SS\'), to_date(\'{faker.date_time_between(start_date='now', end_date='+5y')}\', \'YYYY-MM-DD HH24:MI:SS\'), \
                \'{faker.random_element(elements=('A', 'I'))}\',\
                customer_contact_type(\'{faker.phone_number()}\', \'{faker.email()}\'), 2)\n/\n".replace("                ", " "))
        
        f.write("COMMIT\n/\n")

if __name__ == "__main__":
    n = 10000
    generate_in_migration_inserts(n)
    generate_after_migration_inserts(n)