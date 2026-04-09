// First dropping unique via it's index
db.ConstraintsOnOld_Schema.dropIndex("unique_const_index");

db.ConstraintsOnOld_Schema.createIndex(
    {unique_constraint : 1},
    {name: "unique_index", unique: false}
);

// Making errors moderate
db.runCommand({
    collMod: "ConstraintsOnOld_Schema",
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["not_null_field"],
            properties: {
                "unique_constraint": {
                    bsonType: "number",
                    description: "This field is unique, should lose privilige"
                },
                "check_on_static": {
                    bsonType: "number",
                    description: "This field is more than 0",
                    minimum: 0
                },
                "check_on_other_field": {
                    bsonType: "number",
                    description: "This field's value is less than the next one"
                },
                "ceiler_for_pervious": {
                    bsonType: "number",
                    description: "Ceiler for check_on_other_field"
                },
                "default_constraint": {
                    bsonType: "string",
                    description: "This field has a default value"
                    // Default is not supported in MongoDB
                },
                "not_null_field": {
                    bsonType: "string",
                    description: "This field is not empty"
                }
            }
        },
        $expr: {
         $lt: ["ceiler_for_pervious", "check_on_other_field"]
        }
    },
    validationLevel: "moderate",
    validationAction: "warn"
})

// removing them completely
db.runCommand({
    collMod: "ConstraintsOnOld_Schema",
    validator: {
        $jsonSchema: {
            bsonType: "object",
            properties: {
                "unique_constraint": {
                    bsonType: "number",
                    description: "This field is unique, should lose privilige"
                },
                "check_on_static": {
                    bsonType: "number",
                    description: "This field is more than 0",
                },
                "check_on_other_field": {
                    bsonType: "number",
                    description: "This field's value is less than the next one"
                },
                "ceiler_for_pervious": {
                    bsonType: "number",
                    description: "Ceiler for check_on_other_field"
                },
                "default_constraint": {
                    bsonType: "string",
                    description: "This field has a default value"
                    // Default is not supported in MongoDB
                },
                "not_null_field": {
                    bsonType: "string",
                    description: "This field is not empty"
                }
            }
        }
    },
    validationLevel: "strict",
    validationAction: "warn"
})