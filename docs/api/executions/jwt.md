<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Login and Request a Cognito JWT

The first thing you need to do is obtain a JWT.  You can follow AWS's documentation or our sample code.  

- [AWS Cognito Initiate Authentication API](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html)
- [JWT Overview and sample with curl](../security/jwt.md)

## Example with 🐍 Python

<CodeBlock src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/login_samples/congito_login_http_post.py" lang="python"></CodeBlock>