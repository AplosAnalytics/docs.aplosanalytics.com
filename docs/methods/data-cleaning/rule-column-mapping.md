### Mapping Rule (`mapping`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7604790419161678; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cmgier8y30jewkrn9a1pkbtbz?embed_v=2&utm_source=embed" loading="lazy" title="Column mapping (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Maps data from source columns to destination columns.

| Field | Description | Required |
|--------|------------|----------|
| `columns` | Array of mapping objects with source and destination columns | ✅ Yes |

#### Example:
```json
{
    "type": "mapping",
    "columns": [
        {"source_column": "first_name", "destination_column": "fname"},
        {"source_column": "last_name", "destination_column": "lname"}
    ]
}
```
**Behavior:** Copies data from `first_name` to `fname` and `last_name` to `lname`.