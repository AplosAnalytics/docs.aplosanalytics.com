### Minimum Value Rules (`min`) <!-- TODO: what are all allowed keys for this rule? -->

Get the minimum value from a column and apply it to a destination column.

#### Example:
```json
{
    "type": "min",
    "source_column": "temperature",
    "destination_column": "min_temperature",
}
```
**Behavior:** Captures the minimum value for the column <i>temperature</i> and replicates to a new destination column <i>min_temperature</i>.