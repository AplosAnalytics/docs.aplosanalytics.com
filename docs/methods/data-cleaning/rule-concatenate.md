### Concatenate Rule (`concatenate`)

Trims a value from a source column and copes to a target column.

| Field                | Description                                                                                                                                                                             | Required                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `template`           | Takes a string template containing source column references along with a destination_column, builds a new column value from the template and adds this value to the destination_column. | ✅ Yes                      |
| `delimiter`          | An object containing the characters to use as delimiters.                                                                                                                               | ✅ Yes (default: `'{' '}'`) |
| `value`              | The template value used to build concatenated values.                                                                                                                                   | ✅ Yes                      |
| `destination_column` | The column where concatenated value is copied. Can be an existing or new column.                                                                                                        | ✅ Yes                      |

#### Example:

```json
{
  "description": "Concatenate description",
  "type": "concatenate",
  "template": {
    "delimiter": {
      "start": "{",
      "end": "}"
    },
    "value": "{trta} - {dose} mg - {day}"
  },
  "destination_column": "treatment"
}
```

**Behavior:** Combines `trta`, `dose` and `day` column values into new template string value and copies to the `treatment` column.

| subject | trta         | dose | day | treatment                     |
| ------- | ------------ | ---- | --- | ----------------------------- |
| 1       | SAD Cohort 1 | 50   | 1   | SAD Cohort 1 - 10 mg - Day 1  |
| 1       | SAD Cohort 1 | 50   | 2   | SAD Cohort 1 - 50 mg - Day 2  |
| 1       | SAD Cohort 1 | 100  | 3   | SAD Cohort 1 - 100 mg - Day 3 |
