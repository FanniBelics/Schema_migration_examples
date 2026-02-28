db.divideAndMerge_UpdatedSchema.updateMany(
  {
    schemaVersion: 1,
    field_to_divide_str: { $exists: true }
  },
  [
    {
      $set: {
        delimiterPosition: {
          $indexOfBytes: ["$field_to_divide_str", ","]
        }
      }
    },
    {
      $set: {
        divided_str_p1: {
          $cond: {
            if: { $gt: ["$delimiterPosition", -1] },
            then: {
              $substrBytes: [
                "$field_to_divide_str",
                0,
                "$delimiterPosition"
              ]
            },
            else: {
              $substrBytes: [
                "$field_to_divide_str",
                0,
                5
              ]
            }
          }
        },
        divided_str_p2: {
          $cond: {
            if: { $gt: ["$delimiterPosition", -1] },
            then: {
              $substrBytes: [
                "$field_to_divide_str",
                { $add: ["$delimiterPosition", 2] },
                { $strLenBytes: "$field_to_divide_str" }
              ]
            },
            else: {
              $substrBytes: [
                "$field_to_divide_str",
                5,
                { $strLenBytes: "$field_to_divide_str" }
              ]
            }
          }
        }
      }
    },
    {
      $unset: "delimiterPosition"
    }
  ]
)