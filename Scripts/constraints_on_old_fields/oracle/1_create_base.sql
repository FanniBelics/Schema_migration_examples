-- First we create the base table
create table base_table(
    primary_key number constraint base_pk primary key,
    unique_constraint number(2,0) constraint base_u unique,
    check_on_static number(2,0) constraint base_static_ck check ( check_on_static > 0 ),
    check_on_other_field number(2,0),
    ceiler_for_pervious number(3,0),
    default_constraint varchar2(50) default 'Default',
    not_null_field varchar2(50) constraint base_not_null not null,

    constraint base_table_chk_with_ceiler check ( check_on_other_field < ceiler_for_pervious )
);


