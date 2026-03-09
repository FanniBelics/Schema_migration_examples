-- Create type and add new field
create or replace type wrapper_type as object (
    wrapped_field_1 varchar2(255),
    wrapped_field_2 number(5,3),
    wrapped_field_3 varchar2(15 char)
                                         );

alter table UPDATED_TABLE_2
add wrapper_field wrapper_type;

alter table UPDATED_TABLE_2
add schema_version number(1,0);

-- Adding old schemaNo. before new records come
update UPDATED_TABLE_2
set schema_version = 1
where 1=1;

COMMIT;

-- Adding new schema data
insert into UPDATED_TABLE_2 (ID, OUTER_FIELD_1, WRAPPER_FIELD, OUTER_FIELD_2, SCHEMA_VERSION)
VALUES (4, 'OUTER_OUTER',
        wrapper_type('Experiment1',
                      7.77,
                     'Experiment no1'),
        4,
        2);
commit;
-- Migrate field content to new wrapper type
update UPDATED_TABLE_2
set wrapper_field =
    wrapper_type(FIELD_TO_WRAP_1,
                 FIELD_TO_WRAP_2,
                 FIELD_TO_WRAP_3
             )
where SCHEMA_VERSION = 1;

commit;

select *
from UPDATED_TABLE_2;