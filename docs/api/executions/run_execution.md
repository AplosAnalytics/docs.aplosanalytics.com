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
|`fileId`|yes|The id of the uploaded analysis file (returned by the [upload request](./upload-request) as `data.fileId`).|
|`name`|no|A human-friendly name for the execution.|
|workflow-config block|yes|One of `calculation` (NCA analysis), `data_cleaning`, `custom_calculations`, `custom_plots`, `custom_tables`, or `custom_reports`. The block you include determines the workflow type.|
|`metadata`|no|Caller-defined data stored as-is with the execution (e.g. project id, tags).|

> [!TIP]
> You don't need to hand-author the config block. The web app's wizard produces
> it for you, and the [interactive API reference](https://openapi.aplos-nca.com)
> lets you view and try the full payload for each workflow type.

### Example Payload (NCA Analysis)

Below is a full `calculation` (NCA) queue body. This example is generated from
our OpenAPI specification, so it stays current with the API.

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/payloads/analysis-nca.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/payloads/analysis-nca.json"
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

