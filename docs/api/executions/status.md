<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Get the status of an Execution

An execution will have many status updates along the way.  The primary ones you should trigger off of are.

- QUEUING
- COMPLETE
- FAILED


In general, these are returned in lower-case but may be displayed differently in our UI.
There are several other status updates for generating plots and other output.  But from an application or automation standpoint, the 3 primary statuses above can help you gauge where your analysis is.

## Route
<DisplayRoutes :route-id="['get_status']" :columns-to-show="['path', 'method_type']" />

## Payload
No payload - GET Method


## Response

Currently, the response returns all of the execution information.  This is subject to change to create a lighter response package.  We'll determine the final response by Go-Live Summer 2024.

You can always count on returning an `id` and a `status`.  Official `status_code`s are still being defined.

Once the status is complete, a `presigned` url section will be available containing the url to download your results in a zip format.
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/status-response-payload.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/status-response-payload.json"
    lang="json"    
    :highlightLines="[17,32, 48,49,50,51,52]"
    >
</CodeBlock>

> [!NOTE] 
> The `presigned` section is only available once the status is `complete`
>
> This may be a separate call in the full version of the api.