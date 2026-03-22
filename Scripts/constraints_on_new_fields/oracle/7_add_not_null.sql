-- As null is representing an unknown or non-existant, meaning we need a sign for that

update BASE_TABLE
set TO_BE_NOT_NULL = 'None'
where SCHEMA_VERSION = 1;

-- Now add the not null clause

alter table BASE_TABLE
modify TO_BE_NOT_NULL NOT NULL;

-- Test
-- This should fail
insert into BASE_TABLE(PRIMARY_KEY, TO_BE_NOT_NULL)
VALUES (20, NULL);

-- And these should not
insert into BASE_TABLE(PRIMARY_KEY, TO_BE_NOT_NULL)
VALUES (20, 'NULL');

insert into BASE_TABLE(PRIMARY_KEY, TO_BE_NOT_NULL)
VALUES (21, 'None');

commit;