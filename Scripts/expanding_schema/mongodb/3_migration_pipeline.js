//Addign the new schemaVersion
db.expandingSchema.updateMany(
    {
        field4: {$exists: false}
    },
    {
        $set:{
          schemaVersion: 1
        }
    }
)

//Schema Evolution
db.runCommand({
    collMod: "expandingSchema",
    validator: {
        $jsonSchema: {
            bsonType: "object",
            properties: {
                schemaVersion: {
                    bsonType: "int",
                    enum: [1, 2]
                },
                addedField1: {bsonType: ["int", "null"]},
                addedField2: {bsonType: ["string", "null"]},
                addedField3: {bsonType: ["bool", "null"]}
            }
        }
    },
    validationLevel: "moderate",
    validationAction: "warn"
}
)

//Update old documents (not needed), remove schemaVersion
db.expandingSchema.updateMany({
    schemaVersion: {$exists: true}
},
    { $set:
    {
        schemaVersion: {$exists: false}
    }}
)

//Enforce new schema
db.runCommand({
    collMod: "expandingSchema",
    validator: {
        $jsonSchema: {
            bsonType: "object",
            properties: {
                field1: {bsonType: "int",},
                field2: {bsonType: "string",},
                field3: {bsonType: "bool"},
                addedField1: {bsonType: ["int", "null"]},
                addedField2: {bsonType: ["string", "null"]},
                addedField3: {bsonType: ["bool", "null"]}
            }
        }
    },
    validationLevel: "strict",
    validationAction: "error"
}
)
