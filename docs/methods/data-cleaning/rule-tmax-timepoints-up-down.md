### TMAX Timepoints Rule (`tmax_timepoints_up_down`)

Identifies timepoints relative to TMAX (time of maximum concentration).

| Field | Description | Required |
|--------|------------|----------|
| `compare_column` | Column containing the comparison values | ✅ Yes |

#### Example:
```json
{
    "type": "tmax_timepoints_up_down",
    "source_column": "time",
    "destination_column": "tmax_flag",
    "compare_column": "concentration"
}
```
**Behavior:** Flags timepoints as before, at, or after TMAX based on concentration values.