create or replace type customer_contact_type as object(
    cust_main_phone_number varchar2(25),
    cust_email varchar2(50)
)
/

ALTER TABLE SH.CUSTOMERS
ADD CUSTOMER_CONTACT customer_contact_type
/

ALTER TABLE SH.CUSTOMERS
ADD SCHEMA_VERSION NUMBER(1,0)
/

UPDATE SH.CUSTOMERS
SET SCHEMA_VERSION = 1
WHERE 1=1
/

COMMIT
/

CREATE OR REPLACE TRIGGER SH.CUSTOMERS_CONTACT_TRG
BEFORE INSERT ON SH.CUSTOMERS
FOR EACH ROW
BEGIN
    IF :NEW.SCHEMA_VERSION IS NULL OR :NEW.SCHEMA_VERSION = 1 THEN
        :NEW.CUSTOMER_CONTACT := customer_contact_type(:NEW.cust_main_phone_number, :NEW.cust_email);
    END IF;
END;
/