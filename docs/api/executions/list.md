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
The response contains a list of Executions JSON objects.  Presigned URLs for download will not be available here.  Instead, you will request them.
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/list-response.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/list-response.json"
    lang="json"    
    :highlightLines="[19,34,67,82]"
    >
</CodeBlock>
