<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Security Responses to API Calls

When making API calls, your token will generally tell us if you are allowed to proceed or not.  If the token fails you will get an Authentication or Token Failure / Expiration.

However, there are additional checks within the system.  For instance, you may be a valid user but depending on your role you may not have access to other users executions, etc.  Attempting to act on something not permitted will generate a security warning.

If an internal validation fails you may see an error like the following.  This will result in a 403 error code in the response.



<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/security/security-responses.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/security/security-responses.json"
    lang="json"
    >
</CodeBlock>

