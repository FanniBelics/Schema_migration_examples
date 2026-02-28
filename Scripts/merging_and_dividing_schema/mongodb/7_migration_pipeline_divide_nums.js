//First aspect, simple way of division
db.divideAndMerge_UpdatedSchema.updateMany(
    {
        schemaVersion: 1,
        field_to_divide_num: {$exists: true}
    },
    [{
        $set:{
            divided_num_p1: {
                $trunc: ['$field_to_divide_num', 0]
            },
            divided_num_p2: {
                $mod: ['$field_to_divide_num', 1]
            }
        }
    }]
)

// Second aspect, more complicated solutions, incorrect
db.collection.updateMany(
  {
      schemaVersion:1,
      field_to_divide_num: {$exists: true}
  },
  [
    {
      $set: {
        divided_num_p1: {
          $floor: {
            $divide: [
              { $ln: { $abs: "$field_to_divide_num" } },
              { $ln: 5 }
            ]
          }
        }
      }
    },
    {
      $set: {
        divided_num_p2: {
          $divide: [
            "$field_to_divide_num",
            {
              $pow: [5, "$iterations"]
            }
          ]
        }
      }
    }
  ]
)