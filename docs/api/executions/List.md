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
