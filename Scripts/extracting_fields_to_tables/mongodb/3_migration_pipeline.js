// Setting up schema version
db.extractingCollection.updateMany(
    {},
    {
        $set: {
            schemaVersion: 1
        }
    })

// Adding new fields to the schema
db.runCommand({
    collMod: "extractingCollection",
    validator: {
        $jsonSchema: {
                bsonType: "object",
                properties: {
                    "outer_field_1": {
                        bsonType: "string",
                        description: "This field is not going to move to a new object"
                    },
                    "wrapper":{
                        bsonType: "object",
                        description: "New wrapper object",
                        properties: {
                             "wrapped_field_1": {
                                bsonType: "string",
                                description: "First field wrapped"
                             },
                            "wrapped_field_2": {
                                bsonType: "number",
                                description: "Second field wrapped"
                            },
                            "wrapped_field_3": {
                                bsonType: "string",
                                description: "Third field wrapped"
                            }
                        }
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
                    },
                    "schemaVersion" : {
                        bsonType: "number"
                    }
                }
            }
    },
    validationLevel: "moderate",
    validationAction: "warn"
})

// Insert testing documetn
db.extractingCollection.insertOne({
    outer_field_1: "During migration Documnet",
    wrapper: {
        wrapped_field_1: "First",
        wrapped_field_2: 2,
        wrapped_field_3: "Third field"
    },
    outer_field_2: 17.145,
    schemaVersion: 2
})

// Migrate old elements
db.extractingCollection.updateMany(
    {
        schemaVersion: 1
    },
    [{
        $set: {
            wrapper: {
                wrapped_field_1: "$field_to_wrap_1",
                wrapped_field_2: "$field_to_wrap_2",
                wrapped_field_3: "$field_to_wrap_3",
            },
            schemaVersion: 2
        }
    }]
)