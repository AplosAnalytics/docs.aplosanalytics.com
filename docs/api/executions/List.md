<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# List your executions

If you need to list your executions you can use the following route.


## Route
<DisplayRoutes :route-id="['get_executions']" :columns-to-show="['path', 'method_type']" />

## Payload
No payload - GET method

## Response
The response contains a list of Executions JSON objects.  Presigned URLs for download will not be available here.  Instead, you will request them.
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/list-response.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/list-response.json"
    lang="json"    
    :highlightLines="[17]"
    >
</CodeBlock>
