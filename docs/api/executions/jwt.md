<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Login and Request a Cognito JWT

The first thing you need to do is obtain a JWT.  You can follow AWS's documentation or our sample code.  

- [AWS Cognito Initiate Authentication API](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html)
- [JWT Overview and sample with curl](../security/jwt.md)

## Route
<DisplayRoutes :route-id="['get_jwt']" :columns-to-show="['path', 'method_type']" :display-warnings="false" />

## Payload

### Required Headers
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/login_samples/congito_login_http_post.py" 
    lang="python"
    :displayLines="[{start:12, end: 15}]"
    :showSkippedLinesHelp="false"
></CodeBlock>

### Required Body
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/login_samples/congito_login_http_post.py" 
    lang="python"
    :displayLines="[{start: 17, end: 21}]"
    :showSkippedLinesHelp="false"
></CodeBlock>

## Response

<CodeBlock src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/jwt/cognito-response-payload.json" lang="json"></CodeBlock>


## Example with 🐍 Python

<CodeBlock src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/login_samples/congito_login_http_post.py" lang="python" link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/python/login_samples/congito_login_http_post.py"></CodeBlock>