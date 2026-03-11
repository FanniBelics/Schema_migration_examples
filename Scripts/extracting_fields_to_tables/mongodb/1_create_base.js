db.createCollection("extractingCollection",
    {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                properties: {
                    "outer_field_1": {
                        bsonType: "string",
                        description: "This field is not going to move to a new object"
                    },
                    "field_to_wrap_1": {
                        bsonType: "string",
                        description: "First field to wrap"
                    },
                    "field_to_wrap_2": {
                        bsonType: "number",
                        description: "Second field to wrap"
                    },
                    "field_to_wrap_3": {
                        bsonType: "string",
                        description: "Third field to wrap"
                    },
                    "outer_field_2": {
                        bsonType: "number",
                        description: "Second field not moving to new object"
                    }
                }
            }
        },
         validationLevel: "strict",
         validationAction: "error"
    })