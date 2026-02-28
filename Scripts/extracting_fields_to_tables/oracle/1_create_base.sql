alter session set current_schema  = extract_data_schema;

create table base_table(
    id number primary key,
    outer_field_1 varchar2(50),
    field_to_wrap_1 varchar2(255 char),
    field_to_wrap_2 number(5,3),
    field_to_wrap_3 varchar2(15 char),
    outer_field_2 number(2,0)
);

alter session set current_schema  = extract_data_schema;

create table updated_table(
    id number primary key,
    outer_field_1 varchar2(50),
    field_to_wrap_1 varchar2(255 char),
    field_to_wrap_2 number(5,3),
    field_to_wrap_3 varchar2(15 char),
    outer_field_2 number(2,0)
);

create table updated_table_2(
    id number primary key,
    outer_field_1 varchar2(50),
    field_to_wrap_1 varchar2(255 char),
    field_to_wrap_2 number(5,3),
    field_to_wrap_3 varchar2(15 char),
    outer_field_2 number(2,0)
);