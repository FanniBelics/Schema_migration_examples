db.divideAndMerge_baseSchema.insertMany([
    {
        sample_field: "Sample 1",
        field_to_divide_str: "Delimited, string one",
        field_to_divide_num: 1.19,
        field_to_join_str_p1: "Half string 1",
        field_to_join_str_p2: "Second half 1",
        field_to_join_num_p1: 1.0,
        field_to_join_num_p2: 0.18
    },
    {
        sample_field: "Sample 2",
        field_to_divide_str: "Undelimited string",
        field_to_divide_num: 5.0,
        field_to_join_str_p1: "Half string 2",
        field_to_join_str_p2: "Second half 2",
        field_to_join_num_p1: 4.7,
        field_to_join_num_p2: 1.5
    },
    {
        sample_field: "Sample 3",
        field_to_divide_str: "Delimited, string two",
        field_to_divide_num: 11.73,
        field_to_join_str_p1: "Half string 3",
        field_to_join_str_p2: "Second half 3",
        field_to_join_num_p1: 4.11,
        field_to_join_num_p2: 2.0
    },
    {
        sample_field: "Sample 4",
        field_to_divide_str: "UNDELimited field 2",
        field_to_divide_num: 54.32,
        field_to_join_str_p1: "Half string 4",
        field_to_join_str_p2: "Second half 4",
        field_to_join_num_p1: 2.0,
        field_to_join_num_p2: 111.11
    }

]
)