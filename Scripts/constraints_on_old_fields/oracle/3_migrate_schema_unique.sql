-- Start by adding schema version
alter table CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
add schema_version number(1,0);

update CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
set SCHEMA_VERSION = 1
where 1 = 1;

commit;

-- Removing the unique constraint first
alter table CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
drop constraint BASE_U;

-- Only adding unique for the old records with trigger
create or replace trigger unique_constraint_on_old
before insert
on CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
for each row
declare
    no_of_existing number;
begin
    select count(*)
    into no_of_existing
        from BASE_TABLE
        where SCHEMA_VERSION = 1 and UNIQUE_CONSTRAINT = :NEW.UNIQUE_CONSTRAINT;
    if no_of_existing > 0 and :NEW.SCHEMA_VERSION = 1 then
        raise_application_error(-20000, 'This value should be unique in this schema version!');
    end if;
end;

-- Let's test our constraint
-- This shall fail
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE (PRIMARY_KEY, UNIQUE_CONSTRAINT, NOT_NULL_FIELD, SCHEMA_VERSION)
values (4, 10, 'NOT NULL TEST', 1);
commit;

-- And this should not
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE (PRIMARY_KEY, UNIQUE_CONSTRAINT, NOT_NULL_FIELD, SCHEMA_VERSION)
values (4, 40, 'NOT NULL TEST', 1);
commit;

-- And this neither
insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE (PRIMARY_KEY, UNIQUE_CONSTRAINT, NOT_NULL_FIELD, SCHEMA_VERSION)
values (5, 10, 'NOT NULL TEST', 2);
commit;