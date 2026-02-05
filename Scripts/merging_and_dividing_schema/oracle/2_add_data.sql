insert into MERGE_AND_DIVIDE_SCHEMA.BASE_ENTITY(ID, SAMPLE_FIELD, FIELD_TO_DIVIDE_STR, FIELD_TO_DIVIDE_NUM, FIELD_TO_JOIN_STR_P1, FIELD_TO_JOIN_STR_P2, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (1, 'Sample', 'Delimited, string one', 1.19, 'Half string 1', 'Second half 1', 1, 0.18);

insert into MERGE_AND_DIVIDE_SCHEMA.BASE_ENTITY (ID, SAMPLE_FIELD, FIELD_TO_DIVIDE_STR, FIELD_TO_DIVIDE_NUM,
                                                 FIELD_TO_JOIN_STR_P1, FIELD_TO_JOIN_STR_P2, FIELD_TO_JOIN_NUM_P1,
                                                 FIELD_TO_JOIN_NUM_P2)
values (2, 'Sample text2', 'Undelimited string', 5, 'Half string 2', 'Second half 2', 4.7, 1.5);

insert into MERGE_AND_DIVIDE_SCHEMA.BASE_ENTITY(ID, SAMPLE_FIELD, FIELD_TO_DIVIDE_STR, FIELD_TO_DIVIDE_NUM, FIELD_TO_JOIN_STR_P1, FIELD_TO_JOIN_STR_P2, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (3, 'Sample text 3', 'Delimited, string two', 11.73, 'Half string 3', 'Second half 3', 4.11, 2);

insert into MERGE_AND_DIVIDE_SCHEMA.BASE_ENTITY (ID, SAMPLE_FIELD, FIELD_TO_DIVIDE_STR, FIELD_TO_DIVIDE_NUM, FIELD_TO_JOIN_STR_P1, FIELD_TO_JOIN_STR_P2, FIELD_TO_JOIN_NUM_P1, FIELD_TO_JOIN_NUM_P2)
values (4, 'Sample text 4', 'UNDELimited field 2', 54.32, 'Half string 4', 'Second half 4', 2, 111.11);

commit;