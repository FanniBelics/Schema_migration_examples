-- First the original constraints should be removed

alter table CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
drop constraint base_static_ck;

alter table CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
drop constraint base_table_chk_with_ceiler;

-- Now a trigger should be created to replace the constraints

create or replace trigger check_with_static
before insert
on CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
for each row
    begin
        if(:NEW.CHECK_ON_STATIC < 0 and :new.SCHEMA_VERSION = 1) then
            raise_application_error(-20000, 'This number should be bigger than 0 on the old schema');
        end if;
    end;

create or replace trigger check_with_ceiler
    before insert
    on CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    FOR EACH ROW
    BEGIN
        if(:NEW.CHECK_ON_OTHER_FIELD > :NEW.CEILER_FOR_PERVIOUS and :new.SCHEMA_VERSION = 1) then
            raise_application_error(-20000, 'This number should be bigger than the ceiler on the old schema');
        end if;
    end;

-- Test the trigger:
-- This should raise an error:
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY, CHECK_ON_STATIC,
     CHECK_ON_OTHER_FIELD, CEILER_FOR_PERVIOUS,
     NOT_NULL_FIELD, SCHEMA_VERSION)
VALUES (6, -1, 10, 10, 'NOT NULL', 1);

-- This one as well
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY, CHECK_ON_STATIC,
     CHECK_ON_OTHER_FIELD, CEILER_FOR_PERVIOUS,
     NOT_NULL_FIELD, SCHEMA_VERSION)
VALUES (6, 1, 20, 10, 'NOT NULL', 1);

-- These ones not
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY, CHECK_ON_STATIC,
     CHECK_ON_OTHER_FIELD, CEILER_FOR_PERVIOUS,
     NOT_NULL_FIELD, SCHEMA_VERSION)
VALUES (6, 1, 10, 10, 'NOT NULL', 1);

insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY, CHECK_ON_STATIC,
     CHECK_ON_OTHER_FIELD, CEILER_FOR_PERVIOUS,
     NOT_NULL_FIELD, SCHEMA_VERSION)
VALUES (7, -1, 10, 8, 'NOT NULL', 2);

commit;