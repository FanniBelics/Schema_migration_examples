ALTER TABLE SH.PRODUCTS
ADD SCHEMA_VERSION NUMBER(1,0) DEFAULT 1
/
UPDATE SH.PRODUCTS
SET SCHEMA_VERSION = 1
WHERE 1 = 1
/

CREATE OR REPLACE TRIGGER UNIQUE_ON_PRODUCTS_TGR
BEFORE INSERT 
ON SH.PRODUCTS
FOR EACH ROW
DECLARE
    v_count NUMBER;
BEGIN
    if :NEW.PROD_NAME is not null and :NEW.SCHEMA_VERSION = 2 then
        select count(*)
        into v_count
        from SH.PRODUCTS
        where PROD_NAME = :NEW.PROD_NAME;

        if v_count > 0 then
            raise_application_error(-20000, 'PROD_NAME must be unique in new schema version');
        end if;
    end if;
END;
/