-- First we need schema version
alter table CONSTRAINT_ON_NEW_SCHEMA.BASE_TABLE
add schema_version number(1,0);

update CONSTRAINT_ON_NEW_SCHEMA.BASE_TABLE
set SCHEMA_VERSION = 1
where 1 = 1;

-- Creating trigger on the new constraint

create or replace trigger new_constraint_unique_tgr
before insert
on CONSTRAINT_ON_NEW_SCHEMA.BASE_TABLE
for each row
declare counter number;
begin
    if :new.TO_BE_UNIQUE is not null and :new.SCHEMA_VERSION = 2 then
        select count(*)
        into counter
        from BASE_TABLE
        where TO_BE_UNIQUE = :new.TO_BE_UNIQUE;

        if counter > 0 then
            raise_application_error(-20000, 'This value has to be unique');
        end if;
    end if;
end;

-- Migrate the old elements
-- In order to migrate the old ones, we need to make the to_be_unique truly unique

-- Value gapping way
create table table_with_gapping as
select *
from BASE_TABLE;

alter table table_with_gapping
add to_be_unique_str varchar2(5 char) constraint new_field_unique unique;

create table constraint_value_holders as
select TO_BE_UNIQUE as "VALUE_HELD", count(*) as "APPEARANCE_NO"
from table_with_gapping
group by TO_BE_UNIQUE;

SELECT ROWNUM, TO_BE_UNIQUE
FROM table_with_gapping
WHERE TO_BE_UNIQUE = 1;

CREATE OR REPLACE PROCEDURE MIGRATE_FROM_VALUE_HOLDER is
    GAP_SIZE NUMBER := 10000;
    CURRENT_HEAD NUMBER;
    CURSOR HELD_VALUES is select VALUE_HELD from constraint_value_holders;
begin
    OPEN HELD_VALUES;
    LOOP
        FETCH HELD_VALUES INTO CURRENT_HEAD;
        EXIT WHEN HELD_VALUES%NOTFOUND;
        update table_with_gapping OUTER
        set TO_BE_UNIQUE = CURRENT_HEAD * GAP_SIZE +
            (SELECT ADDITIONAL
            FROM (SELECT table_with_gapping.PRIMARY_KEY AS INNER_PRIMARY, ROWNUM AS "ADDITIONAL"
            FROM table_with_gapping
            WHERE table_with_gapping.TO_BE_UNIQUE = CURRENT_HEAD)
            WHERE OUTER.PRIMARY_KEY = INNER_PRIMARY)
        WHERE TO_BE_UNIQUE = CURRENT_HEAD;
    end loop;
    CLOSE HELD_VALUES;

    COMMIT;
end;

ALTER TABLE table_with_gapping
MODIFY TO_BE_UNIQUE NUMBER(10,0);

BEGIN
    MIGRATE_FROM_VALUE_HOLDER();
END;

ALTER TABLE table_with_gapping
add constraint new_unique_constraint_gapping unique (TO_BE_UNIQUE);

-- Testing
insert into table_with_gapping(PRIMARY_KEY, TO_BE_UNIQUE)
values (10, 30000);

insert into table_with_gapping(PRIMARY_KEY, TO_BE_UNIQUE)
values (11, 10002);

commit;

-- New sequence way

create table table_with_sequence as
select *
from BASE_TABLE;

create sequence migration_seq
start with 1
minvalue 1
nomaxvalue
increment by 1;

update table_with_sequence
set TO_BE_UNIQUE = migration_seq.nextval
where SCHEMA_VERSION = 1;

select *
from table_with_sequence
where SCHEMA_VERSION = 1;

alter table table_with_sequence
add constraint new_unique_constraint unique (TO_BE_UNIQUE);

-- Ubuntu way
create table table_with_allocated_space as
select *
from BASE_TABLE;

--- find the largest number in the field and next number with more digits

SELECT POWER(10, FLOOR(LOG(10, n)) + 1) AS border
FROM (
    select max(TO_BE_UNIQUE) as n
    from table_with_allocated_space
);

create or replace package unique_const_package as
    c_border_value constant number := 10; -- Value gotten from the pervious query

    procedure unique_const_mimic_procedure(
        TO_BE_UNIQUE_FIELD IN NUMBER
    );
end unique_const_package;

create or replace package body unique_const_package as
    procedure unique_const_mimic_procedure(
        TO_BE_UNIQUE_FIELD IN NUMBER
    ) IS
        NO_OF_APPERARANCES NUMBER;
    BEGIN
        IF TO_BE_UNIQUE_FIELD > c_border_value THEN
            SELECT COUNT(*)
            INTO NO_OF_APPERARANCES
            FROM table_with_allocated_space
            where TO_BE_UNIQUE = TO_BE_UNIQUE_FIELD;
            IF NO_OF_APPERARANCES > 0 THEN
                RAISE_APPLICATION_ERROR(-20000, 'This field needs to be unique or stay inside the designated range');
            end if;
        end if;
    end;
end unique_const_package;

create or replace trigger unique_constraint_tgr
before insert
on table_with_allocated_space
for each row
begin
    unique_const_package.unique_const_mimic_procedure(:NEW.TO_BE_UNIQUE);
end;

-- Test the trigger
insert into table_with_allocated_space(PRIMARY_KEY, TO_BE_UNIQUE)
values (4, 5);

insert into table_with_allocated_space(PRIMARY_KEY, TO_BE_UNIQUE)
values (5, 12);

-- This should throw an error
insert into table_with_allocated_space(PRIMARY_KEY, TO_BE_UNIQUE)
values (6, 12);

commit;

-- Unique with new field
create table table_with_sister_field as
select *
from BASE_TABLE;

alter table table_with_sister_field
add sister_field number(2,0) default 1;


update table_with_sister_field OUTER
set sister_field = (
    select appearance
    from ( select PRIMARY_KEY AS INNER_PRIMARY, ROWNUM AS APPEARANCE
            from table_with_sister_field INNER
            where to_be_unique = OUTER.TO_BE_UNIQUE
            AND INNER.SCHEMA_VERSION = 1)
    where INNER_PRIMARY = OUTER.PRIMARY_KEY
    )
where 1 = 1;

commit;

alter table table_with_sister_field
add constraint sister_field_unique unique (TO_BE_UNIQUE, sister_field);

-- Testing
insert into table_with_sister_field (primary_key, TO_BE_UNIQUE)
values (10, 4);
commit;

-- This should throw an error
insert into table_with_sister_field (primary_key, TO_BE_UNIQUE)
values (11, 4);
