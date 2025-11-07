### Text Trimming Rule (`trim_text`)

Trims a value from a source column and copies to a target column.

| Field                | Description                                                                                                                                                                                                                                                                    | Required                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| `source_column`      | The column where values are trimmed from.                                                                                                                                                                                                                                      | ✅ Yes                   |
| `destination_column` | The column where trimmed values are copied. Can be an existing or new column.                                                                                                                                                                                                  | ✅ Yes                   |
| `trim_type`          | Either `left`, `right`, or `middle`. Determines where the trim will start. <ul><li>`left`: Trim from beginning of value to `end_position`</li><li>`right`: Trim from end of value to `start_position`</li><li>`middle`: Trim from `start_position` to `end_position`</li></ul> | ✅ Yes                   |
| `start_position`     | Required for Trim Type `Right` and `Middle`. Any values ignored for Trim Type Left.                                                                                                                                                                                            | ⚠️ Conditional           |
| `end_position`       | Required for Trim Type `Left` and `Middle`. Any values ignored for Trim Type Right.                                                                                                                                                                                            | ⚠️ Conditional           |
| `strict_bounds`      | When attempting to trim data values, determines if index positions that are out of bounds for a value should prevent the rule from completing. If disabled, `destination_column` values for these cases will populate with an error message.                                   | ❌ No (default: `false`) |

#### Example:

```json
{
  "type": "trim_text",
  "source_column": "dose",
  "destination_column": "dose_trimmed",
  "trim_type": "left",
  "start_position": null,
  "end_position": 3,
  "strict_bounds": false
}
```

**Behavior:** Trims values from the `dose` column starting from the left, ending at position 3, and copies to the `dose_trimmed` column.

- "10 mg" ➔ "10 "
- "100 mg" ➔ "100"

```json
{
  "type": "trim_text",
  "source_column": "dose",
  "destination_column": "dose_trimmed",
  "trim_type": "middle",
  "start_position": 2,
  "end_position": 4,
  "strict_bounds": false
}
```

**Behavior:** Trims values from the `dose` column starting from the second position from the left, ending at position 4, and copies to the `dose_trimmed` column.

- "10 mg" ➔ "0 m"
- "100 mg" ➔ "00"
