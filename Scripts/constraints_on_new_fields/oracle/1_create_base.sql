-- Create the base table with no constraints

create table CONSTRAINT_ON_NEW_SCHEMA.base_table(
    primary_key number constraint base_primary_key primary key,
    to_be_unique number(2,0),
    to_be_checked_on_static number(2,0),
    to_be_checked_on_other_field number(2,0),
    soon_to_be_ceiler number(3,0),
    to_be_default varchar2(50),
    to_be_not_null varchar2(50)
);