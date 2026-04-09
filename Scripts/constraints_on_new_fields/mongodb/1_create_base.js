db.createCollection("ConstraintOnNewSchema",
    {
        validator:
            {
                $jsonSchema: {
                    bsonType: "object",
                    properties:{
                        "to_be_unique": {
                            bsonType: "number",
                            description: "This field is going to be unique"
                        },
                        "to_be_checked_on_static": {
                            bsonType: "number",
                            description: "This fields needs to be bigger than 0"
                        },
                        "to_be_checked_on_other_field": {
                            bsonType: "number",
                            description: "Ceiler is going to be added to this field"
                        },
                        "soon_to_be_ceiler": {
                            bsonType: "number",
                            description: "ceiler"
                        },
                        "to_be_not_null": {
                            bsonType: "string",

                        }
                    }
                }
            }
    })