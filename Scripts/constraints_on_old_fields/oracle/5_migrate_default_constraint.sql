-- First drop the constraint

alter table CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
modify default_constraint default NULL;

-- Create trigger to mimic the default

create or replace trigger default_replacement
before insert
on CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
for each row
begin
    if :NEW.SCHEMA_VERSION = 1 then
            :NEW.DEFAULT_CONSTRAINT := 'Default';
    end if;
end;

-- Testing

insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY, NOT_NULL_FIELD, SCHEMA_VERSION)
values (8,  'Not null', 1);
commit;

insert into CONSTRAINT_ON_OLD_SCHEMA.BASE_TABLE
    (PRIMARY_KEY, NOT_NULL_FIELD, SCHEMA_VERSION)
values (9,  'Not null', 2);
commit;
