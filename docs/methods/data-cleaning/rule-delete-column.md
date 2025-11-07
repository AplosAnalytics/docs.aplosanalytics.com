### Delete Column Rule (`delete_column`)

Removes a column from a dataset.

| Field | Description | Required |
|--------|------------|----------|
| `column_name` | Name of the column to delete | ✅ Yes |

#### Example:
```json
{
    "type": "delete_column",
    "column_name": "processed_flag"
}
```
**Behavior:** Deletes the column `processed_flag` from the dataset.