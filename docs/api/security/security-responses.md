<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Security Responses to API Calls

When making API calls, your token will generally tell us if you are allowed to proceed or not.  If the token fails you will get an Authentication or Token Failure / Expiration.

However, there are additional checks within the system.  For instance, you may be a valid user but depending on your role you may not have access to other users executions.

If an internal validation fails you may see an error like the following.

