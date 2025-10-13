### Whitespace Trimming Rule (`trim_whitespace`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7604790419161678; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cmgpeilwd0wly12sxef8b8bxs?embed_v=2&utm_source=embed" loading="lazy" title="Trim whitespace (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Removes leading and trailing whitespace from a text column.

#### Example:
```json
{
    "type": "trim_whitespace",
    "source_column": "email",
    "destination_column": ""
}
```
**Behavior:** Removes extra spaces from the `email` column.