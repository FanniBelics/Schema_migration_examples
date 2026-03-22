-- First create a trigger that replaces the constraint

create or replace trigger static_check_const_tgr
before insert
on BASE_TABLE
for each row
begin
    if :new.SCHEMA_VERSION = 2 and :new.TO_BE_CHECKED_ON_STATIC < :new.SOON_TO_BE_CEILER then
            raise_application_error(-20000, 'In the new schema this value has to be bigger than the ceiler');
    end if;
end;
