create user expanding_schema identified by admin123;

grant connect, resource, dba to expanding_schema;

create user merge_and_divide_schema identified by admin123;
grant connect, resource, dba to merge_and_divide_schema;

create user extract_data_schema identified by admin123;
grant connect, resource, dba to extract_data_schema;
