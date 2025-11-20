### Flag First Observation Rule (`flag_first_observation`)

Identifies first measurable observation and flags that record. This is used in BLQ handling to identify BLQ values before and after the first observation.

| Field | Description | Required |
|--------|------------|----------|
| `source_column` | Column containing the concentration and BLQ values. This rule assumes that numeric values are measurable concentrations. | ✅ Yes |
| `destination_column` | Column to be populated with the values `before`, `at`, or `after` | ✅ Yes |
| `before` | Numeric value populated in `destination_column` for all records before the first numeric value. | ✅ Yes |
| `at` | Numeric value populated in `destination_column` for the record with the first measuraable observation (i.e. first numeric value). | ✅ Yes |
| `after` | Numeric value populated in `destination_column` for all records after the first numeric value. | ✅ Yes |


#### Example:
```json
{
    "type": "flag_first_observation",
    "source_column": "AVALC",
    "destination_column": "blq_flag",
    "before": 0,
    "at": 1,
    "after": 2
}
```
**Behavior:** Flags timepoints as before, at, or after the first measurable concentration based on concentration values. This method assumes ANY numeric value (including 0) is measurable. All BLQ values should have text in the `source_column` for this to work properly.
