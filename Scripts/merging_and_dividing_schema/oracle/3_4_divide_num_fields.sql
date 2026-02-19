-- Here I also test two ways to divide numbers, one simple condition free and a second with condition

-- The first way I want a simple division, where I can remove the numbers after the dot

alter table  UPDATED_ENTITY
modify DIVIDED_NUM_P1 number(6,4);

-- First we can update the already existing records
update UPDATED_ENTITY
set DIVIDED_NUM_P1 = trunc(FIELD_TO_DIVIDE_NUM),
    DIVIDED_NUM_P2 = mod(FIELD_TO_DIVIDE_NUM, 1)
where SCHEMA_VERSION = 1 and FIELD_TO_DIVIDE_NUM is not null;

commit;

-- creating the trigger for the new records
create or replace trigger DIVIDE_NO_AUTOMATICALLY_TGR
    before insert
    on UPDATED_ENTITY
    for each row
begin
    if :new.FIELD_TO_DIVIDE_NUM is not null then
        :new.DIVIDED_NUM_P1 := trunc(:new.FIELD_TO_DIVIDE_NUM);
        :new.DIVIDED_NUM_P2 := mod(:new.FIELD_TO_DIVIDE_NUM, 1);
        :NEW.SCHEMA_VERSION := 1;
    end if;
end;
/

-- Test the trigger
insert into UPDATED_ENTITY(id, SAMPLE_FIELD, FIELD_TO_DIVIDE_NUM)
values (17, 'New sample', 67.66);

insert into UPDATED_ENTITY(id, SAMPLE_FIELD, FIELD_TO_DIVIDE_NUM)
values (18, 'New sample', 2);

commit;

-- Now let's create a more complicated division
-- For this I create a function in the package I created before
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
        n_iterations number;
        origin_field_editable number;
    begin
        n_iterations := 0;
        origin_field_editable := field_from;
        if C_STATIC_NUMBER <> 0 then

        while abs(origin_field_editable)/C_STATIC_NUMBER > 1 loop
            origin_field_editable := origin_field_editable / C_STATIC_NUMBER;
            n_iterations := n_iterations+1;
        end loop;
        end if;
        field_first_part := origin_field_editable;
        field_second_part := n_iterations;
    end;
END DIVISION_PACKAGE;
/

-- Create a trigger on it
create or replace trigger DIVIDE_NO_AUTOMATICALLY_TGR
before insert
on UPDATED_ENTITY
for each row
begin
    if :new.FIELD_TO_DIVIDE_NUM is not null then
        division_package.DIVIDE_NUMS(
            :new.FIELD_TO_DIVIDE_NUM,
            :new.DIVIDED_NUM_P1,
            :new.DIVIDED_NUM_P2
        );
    end if;
end;

-- Test the trigger
insert into UPDATED_ENTITY(id, SAMPLE_FIELD, FIELD_TO_DIVIDE_NUM)
values (19, 'New sample2', 123.66);

insert into UPDATED_ENTITY(id, SAMPLE_FIELD, FIELD_TO_DIVIDE_NUM)
values (20, 'New sample3', -2.22);

insert into UPDATED_ENTITY(id, SAMPLE_FIELD, FIELD_TO_DIVIDE_NUM)
values (21, 'New sample4', 5);

insert into UPDATED_ENTITY(id, SAMPLE_FIELD, FIELD_TO_DIVIDE_NUM)
values (22, 'New sample5', 7);

insert into UPDATED_ENTITY(id, SAMPLE_FIELD, FIELD_TO_DIVIDE_NUM)
values (23, 'New sample5', -7.77);

commit;

-- Now update the old records
-- For this we need a brand-new function that can update our records

CREATE TYPE division_result_type AS OBJECT (
    first_part NUMBER,
    second_part NUMBER);

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

    function divide_on_update(field_from NUMBER)
    return division_result_type;

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
        n_iterations number;
        origin_field_editable number;
    begin
        n_iterations := 0;
        origin_field_editable := field_from;
        if C_STATIC_NUMBER <> 0 then

        while abs(origin_field_editable)/C_STATIC_NUMBER > 1 loop
            origin_field_editable := origin_field_editable / C_STATIC_NUMBER;
            n_iterations := n_iterations+1;
        end loop;
        end if;
        field_first_part := origin_field_editable;
        field_second_part := n_iterations;
    end;

    function divide_on_update(field_from number)
    return division_result_type
    is
        n_iterations number;
        origin_field_editable number;
    begin
        n_iterations := 0;
        origin_field_editable := field_from;

        if C_STATIC_NUMBER <> 0 then
            while abs(origin_field_editable)/C_STATIC_NUMBER > 1 loop
            origin_field_editable := origin_field_editable / C_STATIC_NUMBER;
            n_iterations := n_iterations+1;
        end loop;
        end if;

        return  division_result_type(
                origin_field_editable,
                n_iterations
                );
    end;
END DIVISION_PACKAGE;
/

UPDATE UPDATED_ENTITY entity
SET (DIVIDED_NUM_P1, DIVIDED_NUM_P2) =
(
    SELECT
        division_package.divide_on_update(entity.FIELD_TO_DIVIDE_NUM).first_part,
        division_package.divide_on_update(entity.FIELD_TO_DIVIDE_NUM).second_part
    FROM dual
)
WHERE SCHEMA_VERSION = 1;
;

commit;