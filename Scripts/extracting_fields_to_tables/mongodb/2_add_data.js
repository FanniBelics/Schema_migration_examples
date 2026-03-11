db.extractingCollection.insertMany(
    [{   outer_field_1: "OuterField1",
        field_to_wrap_1: "Wrapped content here",
        field_to_wrap_2: 15.47,
        field_to_wrap_3: "Test1",
        outer_field_2: 1
    },
    {   outer_field_1: "OuterField2",
        field_to_wrap_1: "Wrapped content here",
        field_to_wrap_2: -157,
        field_to_wrap_3: "Test2",
        outer_field_2: 2},
    {
        outer_field_1: "OuterField3",
        field_to_wrap_1: "Wrapped content here",
        field_to_wrap_2: 3,
        field_to_wrap_3: "Test3",
        outer_field_2: 3
    }]
)