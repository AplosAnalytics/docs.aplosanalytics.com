### Count Records Rule (`count_records`)

This rule counts the number of records for each unique group defined by the grouping columns variables.

| Field        | Description                           | Required |
| ------------ | ------------------------------------- | -------- |
| `groupColumns` | Array of columns to group data by each unique combination of values | ✅ Yes   |
| `columName`    | Column where count of records for each group will be output         | ✅ Yes   |

#### Example:

```json
{
  "groupColumns": [
    "subject",
    "route",
    "dose"
  ],
  "columnName": "counts",
  "description": "New rule configuration",
  "type": "count_records"
}
```

**Behavior:** Populates the counts column with a value based on the number of records in the dataset for each combination of subject, route, and dose.
