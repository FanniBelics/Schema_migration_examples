-- By the huge amount of added fields we re-create the table first, then expanding it
create table UPDATED_ENTITY(
    id number primary key,
    sample_field varchar2(50),
    field_to_divide_str varchar2(255 char),
    field_to_divide_num number(5,2),
    field_to_join_str_p1 varchar2(100 char),
    field_to_join_str_p2 varchar2(100 char),
    field_to_join_num_p1 number(5,2),
    field_to_join_num_p2 number(5,2)
);
-- Re-insert Data
insert into MERGE_AND_DIVIDE_SCHEMA.UPDATED_ENTITY(ID, SAMPLE_FIELD, FIELD_TO_DIVIDE_STR, FIELD_TO_DIVIDE_NUM, FIELD_TO_JOIN_STR_P1, FIELD_TO_JOIN_STR_P2, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (1, 'Sample', 'Delimited, string one', 1.19, 'Half string 1', 'Second half 1', 1, 0.18);

insert into MERGE_AND_DIVIDE_SCHEMA.UPDATED_ENTITY (ID, SAMPLE_FIELD, FIELD_TO_DIVIDE_STR, FIELD_TO_DIVIDE_NUM,
                                                 FIELD_TO_JOIN_STR_P1, FIELD_TO_JOIN_STR_P2, FIELD_TO_JOIN_NUM_P1,
                                                 FIELD_TO_JOIN_NUM_P2)
values (2, 'Sample text2', 'Undelimited string', 5, 'Half string 2', 'Second half 2', 4.7, 1.5);

insert into MERGE_AND_DIVIDE_SCHEMA.UPDATED_ENTITY(ID, SAMPLE_FIELD, FIELD_TO_DIVIDE_STR, FIELD_TO_DIVIDE_NUM, FIELD_TO_JOIN_STR_P1, FIELD_TO_JOIN_STR_P2, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (3, 'Sample text 3', 'Delimited, string two', 11.73, 'Half string 3', 'Second half 3', 4.11, 2);

insert into MERGE_AND_DIVIDE_SCHEMA.UPDATED_ENTITY (ID, SAMPLE_FIELD, FIELD_TO_DIVIDE_STR, FIELD_TO_DIVIDE_NUM, FIELD_TO_JOIN_STR_P1, FIELD_TO_JOIN_STR_P2, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (4, 'Sample text 4', 'UNDELimited field 2', 54.32, 'Half string 4', 'Second half 4', 2, 111.11);

commit;

-- adding schema version
alter table UPDATED_ENTITY add SCHEMA_VERSION number(1,0) default 2;

-- Before accepting the new schema, updating schema version on old records
update UPDATED_ENTITY
set UPDATED_ENTITY.SCHEMA_VERSION = 1
where 1 = 1;

commit;

-- Adding updated fields
-- adding new field, which is the added size of the two merged fields
alter TABLE UPDATED_ENTITY ADD MERGED_STRING_FIELD VARCHAR2(210 CHAR);

alter table UPDATED_ENTITY add MERGED_NUMBER_FIELD NUMBER(12,3);

ALTER TABLE UPDATED_ENTITY ADD DIVIDED_STRING_P1 VARCHAR2(255 CHAR);
ALTER TABLE UPDATED_ENTITY ADD DIVIDED_STRING_P2 VARCHAR2(255 CHAR);

ALTER TABLE UPDATED_ENTITY ADD DIVIDED_NUM_P1 NUMBER(5,4);
ALTER TABLE UPDATED_ENTITY ADD DIVIDED_NUM_P2 NUMBER(5,4);

--Adding new data based on the new, expected schema
insert into UPDATED_ENTITY(id, sample_field, field_to_join_num_p1, field_to_join_num_p2,
                           MERGED_STRING_FIELD)
values (5, 'Sample 5', 5, 0.15, 'Merged field 1');

insert into UPDATED_ENTITY(id, sample_field, field_to_join_num_p1, field_to_join_num_p2,
                           MERGED_STRING_FIELD)
values (6, 'Sample 6', 6, 0.16, 'Merged field 2');

insert into UPDATED_ENTITY(id, sample_field, field_to_join_num_p1, field_to_join_num_p2,
                           MERGED_STRING_FIELD)
values (7, 'Sample 7', 7, 0.17, 'Merged field 3');

commit;
-- As we see the schema version field if 2 by default

-- Creating trigger to update schema field automatically
CREATE OR REPLACE TRIGGER update_schema_no_on_insert_tgr
BEFORE INSERT ON updated_entity
FOR EACH ROW
BEGIN
    IF ( :NEW.field_to_join_str_p1 IS NOT NULL AND :NEW.merged_string_field IS NULL )
       OR ( :NEW.field_to_join_num_p1 IS NOT NULL AND :NEW.merged_number_field IS NULL )
       OR ( :NEW.field_to_divide_str IS NOT NULL AND :NEW.divided_string_p1 IS NULL )
       OR ( :NEW.field_to_divide_num IS NOT NULL AND :NEW.divided_num_p1 IS NULL )
    THEN
        :NEW.schema_version := 1;
    END IF;
END;
/
-- Testing
insert into UPDATED_ENTITY (id, field_to_join_str_p1, field_to_join_str_p2)
values (8, 'First half on insert', 'Second half on insert');
commit;

--Creating trigger to automatically update fields
create or replace trigger merge_string_automatically_tgr
before insert
on UPDATED_ENTITY
for each row
begin
    if :new.field_to_join_str_p1 is not null then
        :new.MERGED_STRING_FIELD := :new.field_to_join_str_p1 || ' ' || :new.field_to_join_str_p2;
        :new.schema_version := 1; --optional
    end if;
end;
/

-- Testing
insert into UPDATED_ENTITY (id, field_to_join_str_p1, field_to_join_str_p2)
values (9, 'First half on insert 2', 'Second half on insert 2');
commit;

--Updating already existing data
update UPDATED_ENTITY
set UPDATED_ENTITY.MERGED_STRING_FIELD = FIELD_TO_JOIN_STR_P1 || ' ' || FIELD_TO_JOIN_STR_P2
    --, UPDATED_ENTITY.SCHEMA_VERSION = 2 --In case they are the only/last field to update
where UPDATED_ENTITY.SCHEMA_VERSION = 1;
commit;

-- Remove old fields
/*
ALTER TABLE UPDATED_ENTITY
DROP COLUMN FIELD_TO_JOIN_STR_P1;

ALTER TABLE UPDATED_ENTITY
DROP COLUMN FIELD_TO_JOIN_STR_P2;

DROP TRIGGER MERGE_STRING_AUTOMATICALLY_TGR;
*/

-- If needed run these
/*
ALTER TABLE UPDATED_ENTITY
DROP COLUMN SCHEMA_VERSION;
*/

