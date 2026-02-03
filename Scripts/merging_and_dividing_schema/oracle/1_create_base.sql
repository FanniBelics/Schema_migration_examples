create table base_entity(
    id number primary key,
    sample_field varchar2(50),
    field_to_divide_str varchar2(255 char),
    field_to_divide_num number(5,2),
    field_to_join_str_p1 varchar2(100 char),
    field_to_join_str_p2 varchar2(100 char),
    field_to_join_num_p1 number(5,2),
    field_to_join_num_p2 number(5,2)
);