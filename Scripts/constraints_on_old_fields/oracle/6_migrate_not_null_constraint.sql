-- First drop the constraint

alter table CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
drop constraint base_not_null;

create or replace trigger not_null_constraint_tgr
before insert
ON CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
for each row
begin
    if :NEW.NOT_NULL_FIELD is null and :NEW.SCHEMA_VERSION = 1
        then
            raise_application_error(-20000, 'This field should not be null in the older versions');
    end if;
end;

-- This should raise an error
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY,NOT_NULL_FIELD, SCHEMA_VERSION)
values (10, NULL, 1);

-- This one not
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY,NOT_NULL_FIELD, SCHEMA_VERSION)
values (11, NULL, 2);

-- And neither this one
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY,NOT_NULL_FIELD, SCHEMA_VERSION)
values (10, 'NULL', 1);

commit ;