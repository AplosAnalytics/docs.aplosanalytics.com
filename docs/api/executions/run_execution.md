<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# 🚀 Run an Analysis on the NCA Engine

Once a file is uploaded you can run an NCA Engine Execution against it.  

In general, you can follow the flow of:
1. Uploading a file 
2. Then run an execute action right away

Or 
1. Upload one or more files
2. Run executions at a later date and time. see [Listing Files](../users/list-files.md)

> [!TIP]
> No matter which flow you take,  the execution portion is the same and in this section, we'll take a deeper dive into how to run an execution.

## Route

See [Workflow](../endpoints/routes#workflow) in the API routes reference (Send Analysis to Queue).

## Payload

The queue request body has a small envelope plus one workflow-config block that
determines the workflow type:

|Name|Required|Description|
|--|--|--|
|`fileId`|one of|Entry point for a file-based run (analysis, data-cleaning): the id of the uploaded file (returned by the [upload request](./upload-request) as `data.fileId`).|
|`parentExecutionId`|one of|Entry point for a chained run (custom calculations, plots, tables, reports): the execution this run builds on. Use this instead of `fileId`.|
|`name`|no|A human-friendly name for the execution.|
|workflow-config block|yes|One of `calculation` (NCA analysis), `data_cleaning`, `custom_calculations`, `custom_plots`, `custom_tables`, or `custom_reports` — the block you include determines the workflow type. Exception: `custom_plots` and `custom_tables` may be sent together in one body to run simultaneously.|
|`metadata`|no|Caller-defined data stored as-is with the execution (e.g. project id, tags).|

> [!TIP]
> You don't need to hand-author the config block. The web app's wizard produces
> it for you, and the [interactive API reference](https://openapi.aplos-nca.com)
> lets you view and try the full payload for each workflow type.
>
> Inside `data_cleaning.rules` and `custom_calculations.calculations`, each item
> is self-describing by its `type` — the keys it accepts (and the column names /
> values it references) depend on that rule/calculation type and your input data.
> The examples below show representative shapes.

### Example: NCA Analysis

A full `calculation` (NCA) queue body — entry point is `fileId`. Generated from
our OpenAPI specification, so it stays current with the API.

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/payloads/analysis-nca.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/payloads/analysis-nca.json"
    lang="json"    
    >
</CodeBlock>

### Example: Custom Calculations

A `customCalculations` queue body — chains off a prior run via
`parentExecutionId`. Each entry in `calculations[]` is typed (here, `ratio`).

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/payloads/custom-calculations.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/payloads/custom-calculations.json"
    lang="json"    
    >
</CodeBlock>

### Example: Custom Plots & Tables

A post-processing body chaining off a prior run via `parentExecutionId`.
`customPlots` and `customTables` can each be sent **on their own**, or **together
in one body** — a distinctive capability that lets plots and tables run
simultaneously (shown below). Each entry in `plots[]` / `tables[]` is typed (e.g.
`individual_linear`, `summary_pk_parameters`).

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/payloads/custom-plots-tables.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/payloads/custom-plots-tables.json"
    lang="json"    
    >
</CodeBlock>

> [!NOTE]
> Request and response fields use `camelCase` to match the web app. You can
> request `snake_case` instead via the API's case option if your integration
> prefers it.


## Response

The analysis is accepted onto the workflow queue and the response returns
`data.executionId` and `data.status` (`queued`, or `throttled` with a
`delaySeconds` when admission is delayed). Use the `executionId` to
[poll for status](./status).

> [!NOTE]
> The `data` payload is returned in `camelCase` to match the web app. You can
> request `snake_case` instead via the API's case option if your integration prefers it.

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/run_execution_response.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/run_execution_response.json"
    lang="json"    
    >
</CodeBlock>


## Example with 🐍 Python

Example of how an execution is launched.

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/aplos_nca/main.py"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/python/aplos_nca/main.py"
    lang="python"    
    :displayLines="[{start: 92, end: 143}]"
    >
</CodeBlock>

