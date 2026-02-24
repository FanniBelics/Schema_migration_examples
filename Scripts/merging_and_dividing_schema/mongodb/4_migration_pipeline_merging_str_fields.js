// Add new fields to the database
db.runCommand({
    collMod: "divideAndMerge_UpdatedSchema",
    validator: {
        $jsonSchema:{
                bsonType: "object",
                properties: {
                    sample_field:{
                        bsonType: "string",
                        description: "Sample field, represents unused fields"
                        },
                    field_to_divide_str:{
                        bsonType: "string",
                        description: "String that is going to be divided"
                        },
                    field_to_divide_num:{
                        bsonType: ["int","double"],
                        description: "doubleeger that is going to be divided"
                    },
                    field_to_join_str_p1:{
                        bsonType: "string",
                        description: "The first part of the merged string"
                    },
                    field_to_join_str_p2:{
                        bsonType: "string",
                        description: "The second part of the merged string"
                    },
                    field_to_join_num_p1:{
                        bsonType: ["int","double"],
                        description: "The first part of the merged number"
                    },
                    field_to_join_num_p2:{
                        bsonType: ["int","double"],
                        description: "The second part of the merged number"
                    },
                    schemaVersion:{
                        bsonType: "int",
                        description: "Schema version"
                    },
                    merged_str_field:{
                        bsonType: "string",
                        description: "Merged string, since version 2"
                    }
                    }
                }
                },
    validationLevel: "moderate",
    validationAction: "warn"
});

// Add some version 2 test data
db.divideAndMerge_UpdatedSchema.insertMany([
    {
        sample_field : "Test Data For str merge 1",
        merged_str_field: "Merged STR field, no worries",
        schemaVersion: 2
    },
    {
        sample_field : "Test Data For str merge 2",
        merged_str_field: "Merged STR field 2 no worries",
        schemaVersion: 2
    }
]
)

// Add the merging algorithm

db.divideAndMerge_UpdatedSchema.updateMany(
    {
        schemaVersion:1
    },
    [{
        $set: {
            merged_str_field :
                {$concat: ["$field_to_join_str_p1", " ", "$field_to_join_str_p2"]}
        }
    }]
)
