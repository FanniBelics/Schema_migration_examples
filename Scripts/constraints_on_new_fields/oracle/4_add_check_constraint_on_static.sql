-- First create a trigger that replaces the constraint

create or replace trigger static_check_const_tgr
before insert
on BASE_TABLE
for each row
begin
    if :new.SCHEMA_VERSION = 2 and :new.TO_BE_CHECKED_ON_STATIC < 0 then
            raise_application_error(-20000, 'In the new schema this value has to be bigger than 0');
    end if;
end;

-- Migrate the old elements to the new schema
alter table BASE_TABLE
add multiplier number (1,0) default 1;

update BASE_TABLE
set multiplier = -1,
    TO_BE_CHECKED_ON_STATIC = TO_BE_CHECKED_ON_STATIC * -1
where SCHEMA_VERSION = 1 and TO_BE_CHECKED_ON_STATIC < 0;

alter table BASE_TABLE
add constraint static_check_const check ( TO_BE_CHECKED_ON_STATIC > 0 );