-- Adding default to a table is not restraining

alter table BASE_TABLE
modify TO_BE_DEFAULT VARCHAR2(50) default 'New Default';