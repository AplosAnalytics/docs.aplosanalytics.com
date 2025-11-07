### Text Trimming Rule (`trim_text`)

Trims a value from a source column and copies to a target column.

| Field                | Description                                                                                                                                                                                                                                                                    | Required                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| `source_column`      | The column where values are trimmed from.                                                                                                                                                                                                                                      | ✅ Yes                   |
| `destination_column` | The column where trimmed values are copied. Can be an existing or new column.                                                                                                                                                                                                  | ✅ Yes                   |
| `trim_value`         | Must be either `none`, `left`, `right`, or `both`. Controls how `destination_column` final values are trimmed.                                                                                                                                                                 | ✅ Yes (default: `none`) |
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
  "trim_value": "right",
  "trim_type": "left",
  "start_position": null,
  "end_position": 3,
  "strict_bounds": false
}
```

**Behavior:** Trims values from the `dose` column starting from the 1st character, and ending at the 3rd character, and copies to the `dose_trimmed` column. Note that `trim_value` is set to `right` which removes trailing whitespace.

- "10 mg" ➔ "10"
- "100 mg" ➔ "100"

```json
{
  "type": "trim_text",
  "source_column": "dose",
  "destination_column": "dose_trimmed",
  "trim_value": "none",
  "trim_type": "middle",
  "start_position": 2,
  "end_position": 4,
  "strict_bounds": false
}
```

**Behavior:** Trims values from the `dose` column starting from the 2nd character, ending at the 4th character, and copies to the `dose_trimmed` column.

- "10 mg" ➔ "0 m"
- "100 mg" ➔ "00"

```json
{
  "type": "trim_text",
  "source_column": "day",
  "destination_column": "day_trimmed",
  "trim_type": "right",
  "start_position": 4,
  "trim_value": "none",
  "strict_bounds": false
}
```

**Behavior:** Trims values from the `day` column starting at the 4th character, and ending at the end of the value, and copies to the `day_trimmed` column. Note that `trim_value` is set to `none` so white space is preserved.

- "Day 1"  ➔ " 1"
- "Day 14" ➔ " 14"
- "Days 28" ➔ "s 28"


```json
{
  "type": "trim_text",
  "source_column": "day",
  "destination_column": "day_trimmed",
  "trim_type": "right",
  "start_position": -2,
  "trim_value": "left",
  "strict_bounds": false
}
```

**Behavior:** Trims values from the `day` column starting -2 positions from the right, and ending at the end of the value, and copies to the `day_trimmed` column. Note that `trim_value` is set to `right` which removes trailing whitespace.

- "Day 1"  ➔ "1"
- "Day 14" ➔ "14"
- "Day 28" ➔ "28"
