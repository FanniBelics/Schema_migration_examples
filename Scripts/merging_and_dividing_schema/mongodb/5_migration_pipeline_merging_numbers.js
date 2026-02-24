//Update the schema
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
                    },
                    merged_num_field:{
                        bsonType: "number",
                        description: "Merged number, since version 2"
                        }
                    }
                }
                },
    validationLevel: "moderate",
    validationAction: "warn"
});

// First version, merging numbers by multiplication
db.divideAndMerge_UpdatedSchema.updateMany(
    {
        $and:[
            {schemaVersion:1},
            {field_to_join_num_p1: {$exists: true}}
            ]
    },
    [{
        $set: {
            merged_num_field : {
                $multiply: ["$field_to_join_num_p1", "$field_to_join_num_p2"]
            }
            }
    }]
)

// Second version, merge with decision
db.divideAndMerge_UpdatedSchema.updateMany(
  {
    schemaVersion: 1,
    field_to_join_num_p1: { $exists: true }
  },
  [
    {
      $set: {
        merged_num_field: {
          $cond: {
            if: {
              $eq: [
                { $mod: ["$field_to_join_num_p1", 2] },
                0
              ]
            },
            then: {
              $multiply: [
                "$field_to_join_num_p1",
                "$field_to_join_num_p2"
              ]
            },
            else: {
              $multiply: [
                { $add: ["$field_to_join_num_p1", 1] },
                "$field_to_join_num_p2"
              ]
            }
          }
        }
      }
    }
  ]
)