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

## Response