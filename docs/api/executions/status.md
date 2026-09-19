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
<DisplayRoutes :route-id="['get_status']" />

## Payload
No payload - GET Method


## Response

The response returns the full execution record. You can always count on an `id`
and a `status` being present.

Once the status is complete, output files are available to download. Use the
execution outputs routes to list and retrieve them.
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