<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# List your executions

If you need to list your executions you can use the following route.


## Route

See [Workflow](../endpoints/routes#workflow) in the API routes reference (Get Execution History).

## Payload
No payload - GET method

## Response

The response is wrapped in the standard success envelope. `data.executions` is
an array of execution records, `data.count` is the number returned on this page,
and `data.nextKey` is an opaque pagination token — pass it as `start_key` on the
next request to fetch the following page (`null` when there are no more pages).

Download URLs are not included here. Once an execution has `succeeded`, retrieve
its output files via the execution outputs routes (see
[Workflow](../endpoints/routes#workflow)).

> [!NOTE]
> You can send request fields in `camelCase` or `snake_case` — the API accepts
> either and normalizes to `snake_case` internally. Responses come back in
> `camelCase` to match the web app.

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/list-response.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/list-response.json"
    lang="json"    
    >
</CodeBlock>
