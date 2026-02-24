// Update pre-existing documents with schemaVersion
db.divideAndMerge_UpdatedSchema.updateMany(
    {

    },
    {
        $set:{
            schemaVersion: 1
        }
    }
);