### Find & Replace Rule (`find_replace`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7604790419161678; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cmgidpove0ikfkrn9wm1cca76?embed_v=2&utm_source=embed" loading="lazy" title="Find & Replace (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Replaces occurrences of a specified value in a column.

| Field | Description | Required |
|--------|------------|----------|
| `find` | The text or pattern to search for. | ✅ Yes |
| `replace` | The text to replace matches with. | ✅ Yes |
| `regex` | If `true`, the `find` field will be treated as a regular expression. | ❌ No (default: `false`) |

#### Example:
```json
{
    "type": "find_replace",
    "source_column": "customer_name",
    "destination_column": "",
    "find": "Inc\.",
    "replace": "Incorporated",
    "regex": true
}
```
**Behavior:** Replaces "Inc." with "Incorporated" in the `customer_name` column.