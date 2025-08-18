### Maximum Value Rules (`max`)

Get the maximum value from a column and apply it to a destination column

#### Example:
```json
{
    "type": "max",
    "source_column": "temperature",
    "destination_column": "max_temperature",
}
```
**Behavior:** Captures the maximum value for the column <i>temperature</i> and replicates to a new destination column <i>max_temperature</i>.