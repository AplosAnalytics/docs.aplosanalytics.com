<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Get the status of an Execution

An execution moves through several states. The top-level `data.status` values you
should trigger off of are:

- `queued` — accepted and waiting to start
- `running` — in progress (see `data.statusMessage`, e.g. "Running: Packaging results")
- `succeeded` — finished successfully
- `failed` — finished with an error (see `data.errorCode` and `data.errors`)

While `running`, `data.phases[].steps[]` shows fine-grained progress (each step
has its own `status`, `durationHuman`, and sometimes a `stats` object). This is
informational — for automation, the four top-level statuses above are what you
gauge completion on.

## Route

See [Workflow](../endpoints/routes#workflow) in the API routes reference (Get Execution Status).

## Payload
No payload - GET Method


## Response

The response is wrapped in the standard success envelope. `data` is the full
execution record — you can always count on `data.id` and `data.status` being
present, along with `data.progress`, `data.phases`, and `data.packageAvailable`.

Once `data.status` is `succeeded`, `data.packageAvailable` becomes `true` and the
generated output package appears under `data.phases[].outputs[]` (each output has
a `fileId`, `fileName`, `outputType`, and `ready` flag). Download the file by its
`fileId` via the execution outputs routes (see
[Workflow](../endpoints/routes#workflow)) — retrieval is a separate call, not an
embedded download URL.

> [!NOTE]
> The `data` payload is returned in `camelCase` to match the web app. You can
> request `snake_case` instead via the API's case option if your integration prefers it.

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/status-response-payload.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/status-response-payload.json"
    lang="json"    
    >
</CodeBlock>


## Handling Failures

When `data.status` is `failed`, the record includes structured error detail:

- `data.error` — the first (primary) error.
- `data.errors[]` — all errors (the first element matches `data.error`).

Each error object carries a machine-readable `code` (e.g. `DATA_CLEANING_RULE_ERROR`),
a human-readable `message`, the `phase` and `step` where it occurred, and a
`details` object with context specific to that error (for a data-cleaning rule
failure, for example, `details.ruleType`, `details.reason`, and the
`details.availableColumns` present in the file).

The `data.phases[].steps[]` array also pinpoints which step failed — the failing
step's `status` is `failed` while the others report `succeeded` or `pending`.

> [!TIP]
> A `failed` execution may still produce a partial output package
> (`data.packageAvailable` can be `true`) — for example, a data-cleaning run that
> fails a rule may still package diagnostics. Always branch on `data.status`, not
> on `data.packageAvailable`, to decide success.

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/status-response-failed.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/status-response-failed.json"
    lang="json"    
>
</CodeBlock>
