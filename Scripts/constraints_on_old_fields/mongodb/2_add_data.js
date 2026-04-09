db.ConstraintsOnOld_Schema.insertMany([
    {
        unique_constraint: 10,
        check_on_static: 13,
        check_on_other_field: 10,
        ceiler_for_pervious: 50,
        default_constraint: "Not Default Value",
        not_null_field: "Not null"
    },
    {
        unique_constraint: 20,
        check_on_static: 15,
        check_on_other_field: 4,
        ceiler_for_pervious: 7,
        not_null_field: "Not null"
    },
    {
        unique_constraint: 30,
        check_on_static: 99,
        check_on_other_field: 49,
        ceiler_for_pervious: 50,
        default_constraint: "Not default Value 2",
        not_null_field: "Not null 2"
    }
    ])