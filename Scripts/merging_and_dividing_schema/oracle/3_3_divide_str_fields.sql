-- Dividing strings can happen on a fixed length or based on a delimiter
-- In this file I am going to attempt both with different procedures

create or replace procedure divide_already_existing_strings(
    delimiter IN varchar2,
    fixed_length IN number
) is
begin
    -- If string has the delimiter divide it by that
        update UPDATED_ENTITY
        set DIVIDED_STRING_P1 = substr(FIELD_TO_DIVIDE_STR, 1, instr(FIELD_TO_DIVIDE_STR, delimiter)-1),
            DIVIDED_STRING_P2 = SUBSTR(FIELD_TO_DIVIDE_STR, INSTR(FIELD_TO_DIVIDE_STR, delimiter)+2)
        where instr(FIELD_TO_DIVIDE_STR, delimiter) > 0;
    -- If not divide by the 5th character (if exists)
    update UPDATED_ENTITY
    set DIVIDED_STRING_P1 = substr(FIELD_TO_DIVIDE_STR, 1, fixed_length),
        DIVIDED_STRING_P2 = substr(FIELD_TO_DIVIDE_STR, fixed_length+1)
    where instr(FIELD_TO_DIVIDE_STR, delimiter) = 0;

    COMMIT;
end;

-- Calling procedure to schema-migrate old records
begin
    divide_already_existing_strings(',', 5);
end;

-- The perviously wrote UPDATE_SCHEMA_NO_ON_INSERT_TGR takes care of new records SchemaVersion
insert into UPDATED_ENTITY(id, FIELD_TO_DIVIDE_STR)
values (13, 'DeliMiTed, FiELD');

insert into UPDATED_ENTITY(id, FIELD_TO_DIVIDE_STR)
values (14, 'UnDeLiMiTed FiElD');

commit;

-- It still seems to be possible to write a whole trigger on this, so we can keep on migrating schema
-- Even if the record arrives in the old schema

-- In order to replace the delimiter parameter we need to find a way to store it in the database
-- For this let's create a package

create or replace package division_package as
    c_delimiter CONSTANT VARCHAR2(1 CHAR) := ',';
    c_static_number CONSTANT NUMBER(1,0) := 5;

    procedure divide_strings(
        field_from IN VARCHAR2,
        field_first_part OUT VARCHAR2,
        field_second_part OUT VARCHAR2
    );

    procedure divide_nums(
        field_from IN NUMBER,
        field_first_part OUT NUMBER,
        field_second_part OUT NUMBER
    );

END division_package;

create or replace package body division_package as
    PROCEDURE divide_strings(
        field_from IN VARCHAR2,
        field_first_part OUT VARCHAR2,
        field_second_part OUT VARCHAR2
    ) is
    delimiter_position NUMBER;
        begin
            delimiter_position := instr(field_from, c_delimiter);

            IF delimiter_position > 0 THEN
                field_first_part := substr(field_from, 1, delimiter_position-1);
                field_second_part := substr(field_from, delimiter_position+2);
            else
                field_first_part := substr(field_from, 1, c_static_number);
                field_second_part := substr(field_from, c_static_number+1);
            end if;
        end;

    PROCEDURE DIVIDE_NUMS(
        field_from IN NUMBER,
        field_first_part OUT NUMBER,
        field_second_part OUT NUMBER
    )
    IS
    begin
        DBMS_OUTPUT.PUT_LINE('Implemented later on');
    end;
END DIVISION_PACKAGE;

create or replace trigger DIVIDE_STRINGS_AUTOMATICALLY_ON_INSERT
BEFORE INSERT
ON UPDATED_ENTITY
FOR EACH ROW
BEGIN
    IF :NEW.FIELD_TO_DIVIDE_STR IS NOT NULL THEN
        division_package.divide_strings(
            :new.FIELD_TO_DIVIDE_STR,
            :new.DIVIDED_STRING_P1,
            :new.DIVIDED_STRING_P2
        );
    end if;
end;

-- Let's try the trigger
insert into UPDATED_ENTITY(id, FIELD_TO_DIVIDE_STR)
values (15, 'DeliMiTed, FiELD');

insert into UPDATED_ENTITY(id, FIELD_TO_DIVIDE_STR)
values (16, 'UnDeLiMiTed FiElD');

commit;