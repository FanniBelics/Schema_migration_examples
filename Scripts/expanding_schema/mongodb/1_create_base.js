db.createCollection("expandingSchema",
    {
        validator: {
            $jsonSchema:{
                bsonType: "object",
                properties: {
                    field1: {
                        bsonType: "int",
                        description: "Field No. 1"
                    },
                    field2: {
                        bsonType: "string",
                        description: "Field No. 2"
                    },
                    field3: {
                        bsonType: "bool",
                        description: "Field No. 3"
                    },
                }
            }
        },
        validationLevel: "strict"
    })