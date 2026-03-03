-- First solution, creating a wrapper field with 1-N relationships

create table wrapper(
    id number,
    main_entity_id number constraint main_entity_fk references UPDATED_TABLE(ID),
    field_to_wrap_1 varchar2(255 char),
    field_to_wrap_2 number(5,3),
    field_to_wrap_3 varchar2(15 char)
);

-- This way each main entity is able to have more than one wrapper

-- Adding existing data to the new table

create sequence wrapper_seq
start with 1
increment by 1
minvalue 1
nomaxvalue
nocycle;

-- Migrate the existing ones
insert into wrapper(id, main_entity_id, field_to_wrap_1, field_to_wrap_2, field_to_wrap_3)
select wrapper_seq.nextval, id, FIELD_TO_WRAP_1, FIELD_TO_WRAP_2, FIELD_TO_WRAP_3
    from UPDATED_TABLE;

select *
from wrapper;

commit;

-- Now we could move the old values, but let's upgrade the new record with old schemas as well
create or replace trigger migrate_to_wrapper
after insert
on UPDATED_TABLE
for each row
begin
    insert into wrapper (id, main_entity_id, field_to_wrap_1, field_to_wrap_2, field_to_wrap_3)
    values (wrapper_seq.nextval, :new.id, :NEW.FIELD_TO_WRAP_1, :NEW.FIELD_TO_WRAP_2, :new.FIELD_TO_WRAP_3);
end;

-- Test the trigger
insert into UPDATED_TABLE(ID, OUTER_FIELD_1, FIELD_TO_WRAP_1, FIELD_TO_WRAP_2, FIELD_TO_WRAP_3, OUTER_FIELD_2)
values (4, 'OuterNew', 'New wrapper', 15.44, 'Neww wraappeerr', 32);

select *
from UPDATED_TABLE main_entity inner join wrapper w on main_entity.ID = w.main_entity_id;

insert into wrapper(id, main_entity_id, field_to_wrap_1, field_to_wrap_2, field_to_wrap_3)
values (5, 1, 'Wrapalone', 44, 'ABCDEF');

-- If we left something out, we can always make sure to update with an insert statement
insert into wrapper(id, main_entity_id, field_to_wrap_1, field_to_wrap_2, field_to_wrap_3)
select wrapper_seq.nextval, id, FIELD_TO_WRAP_1, FIELD_TO_WRAP_2, FIELD_TO_WRAP_3
    from UPDATED_TABLE;
