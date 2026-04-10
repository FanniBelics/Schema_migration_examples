db.runCommand({
    collMod: "ConstraintOnNewSchema",
    validator: {
        $jsonSchema: {
                    bsonType: "object",
                    required: ["to_be_not_null"],
                    properties:{
                        "to_be_unique": {
                            bsonType: "number",
                            description: "This field is going to be unique"
                        },
                        "to_be_checked_on_static": {
                            bsonType: "number",
                            description: "This fields needs to be bigger than 0",
                            minimum: 0
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
                },
        $expr: {
         $lt: ["$to_be_checked_on_other_field", "$soon_to_be_ceiler"]
        }
    },
    validationLevel: "moderate",
    validationAction: "warn"
});

//Unique needs to be migrated for the index
db.ConstraintOnNewSchema.updateMany(
    {},
    {
        $set:{
            schemaVersion: 1
        }
    }
);


db.ConstraintOnNewSchema.aggregate([
  {
    $setWindowFields: {
      partitionBy: "$to_be_unique",
      sortBy: { _id: 1 },
      output: {
        dupIndex: { $documentNumber: {} }
      }
    }
  },
  {
    $set: {
      to_be_unique: {
        $cond: {
          if: { $eq: ["$schemaVersion", 1] },
          then: {
            $add: [
              { $multiply: ["$to_be_unique", 10000] },
              "$dupIndex"
            ]
          },
          else: "$to_be_unique"
        }
      }
    }
  },
  { $unset: "dupIndex" },
  {
    $merge: {
      into: "ConstraintOnNewSchema",
      whenMatched: "merge",
      whenNotMatched: "discard"
    }
  }
])

// Now adding the unique
db.ConstraintOnNewSchema.createIndex(
    {to_be_unique : 1},
    {name: "unique_const_index_new", unique: true}
);

db.ConstraintOnNewSchema.updateMany(
    {},
    {
        $unset: {schemaVersion: ""}
    }
);

// Make constraint strict
db.runCommand({
    collMod: "ConstraintOnNewSchema",
    validator: {
        $jsonSchema: {
                    bsonType: "object",
                    required: ["to_be_not_null"],
                    properties:{
                        "to_be_unique": {
                            bsonType: "number",
                            description: "This field is going to be unique"
                        },
                        "to_be_checked_on_static": {
                            bsonType: "number",
                            description: "This fields needs to be bigger than 0",
                            minimum: 0
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
                },
        $expr: {
         $lt: ["$to_be_checked_on_other_field", "$soon_to_be_ceiler"]
        }
    },
    validationLevel: "strict",
    validationAction: "error"
});