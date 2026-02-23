db.createCollection("divideAndMerge_baseSchema",
{
        validator:{
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
                    }
                    }
                }
                }
    })