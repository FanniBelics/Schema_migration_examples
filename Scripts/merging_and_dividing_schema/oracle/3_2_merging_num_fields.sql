/*
-- adding schema version
alter table UPDATED_ENTITY add SCHEMA_VERSION number(1,0) default 2;

-- Before accepting the new schema, updating schema version on old records
update UPDATED_ENTITY
set UPDATED_ENTITY.SCHEMA_VERSION = 1
where 1 = 1;

commit;
*/

-- alter table UPDATED_ENTITY add MERGED_NUMBER_FIELD NUMBER(12,3);

-- Simpler way of merging numbers
-- This example creates a simple merging of numbers, n*m, like gross * vat rate = net
create or replace trigger merge_no_automatically_tgr
before insert
on UPDATED_ENTITY
for each row
    begin
        if :new.FIELD_TO_JOIN_NUM_P1 is not null and :new.FIELD_TO_JOIN_NUM_P2 is not null then
            :new.MERGED_NUMBER_FIELD := :new.FIELD_TO_JOIN_NUM_P1 * :new.FIELD_TO_JOIN_NUM_P2;
            :new.SCHEMA_VERSION := 1;
        end if;
    end;
/

-- Testing
insert into UPDATED_ENTITY (id, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (10, 10.12, 8.7);

commit;

-- Adding more complicated logic for calculation
/*
    I also want to test if we are able to make changes on more complicated business logic, for this
    I'm taking even and odd numbers, if the number is even I simply multiply, if not, I add one then multiply
*/
create or replace trigger merge_no_automatically_tgr
before insert
on UPDATED_ENTITY
for each row
begin
    if MOD(:new.FIELD_TO_JOIN_NUM_P1,2) = 0 then
        :new.MERGED_NUMBER_FIELD := :new.FIELD_TO_JOIN_NUM_P1 * :new.FIELD_TO_JOIN_NUM_P2;

    else
        :new.MERGED_NUMBER_FIELD := (:new.FIELD_TO_JOIN_NUM_P1+1) * :new.FIELD_TO_JOIN_NUM_P2;
    end if;
    :new.SCHEMA_VERSION := 1;
end;

insert into UPDATED_ENTITY(id, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (11, 1, 4.5);

insert into  UPDATED_ENTITY(id, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (12, 2, 4.5);

commit;

-- Update existing values if any
update UPDATED_ENTITY
set MERGED_NUMBER_FIELD = FIELD_TO_JOIN_NUM_P1 * FIELD_TO_JOIN_NUM_P2
-- ,schema_version = 2
where SCHEMA_VERSION = 1 and mod(FIELD_TO_JOIN_NUM_P1, 2) = 0;

update UPDATED_ENTITY
set MERGED_NUMBER_FIELD = (FIELD_TO_JOIN_NUM_P1 + 1) * FIELD_TO_JOIN_NUM_P2
-- ,schema_version = 2
where SCHEMA_VERSION = 1 and mod(FIELD_TO_JOIN_NUM_P1, 2) = 1;

-- Remove old fields if necessary
/*
ALTER TABLE UPDATED_ENTITY
DROP COLUMN FIELD_TO_JOIN_NUM_P1;

ALTER TABLE UPDATED_ENTITY
DROP COLUMN FIELD_TO_JOIN_NUM_P2;

DROP TRIGGER MERGE_NO_AUTOMATICALLY_TGR;
*/

-- If needed run these
/*
ALTER TABLE UPDATED_ENTITY
DROP COLUMN SCHEMA_VERSION;
*/