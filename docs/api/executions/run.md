<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# 🚀 Run an Analysis on the NCA Engine



## Route
<DisplayRoutes :route-id="['run_execution']" :columns-to-show="['path', 'method_type']" />

## Payload
To run an analysis, you need to provide two required sections of the payload and an optional set of meta-data.

|Name|Description|
|--|--|
|The Analysis File|You'll need the S3 bucket and the Object Key which was returned to you during the presigning process.  You can also get a list of files available to you through an API call.|
|The Configuration|supplied in JSON format|
|Meta Data|Optional: Supplied in JSON format or text.  This is stored "as-is" in the record and you can use to as you see fit.  Example uses: Tracking id's for internal use.  Tagging Team members etc.|


### Payload Example

Below is a sample of the payload required for submission.  For this sample, we excluded the meta-data.
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/payloads/payload_sample.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/payloads/payload_sample.json"
    lang="json"    
    :displayLines="[{start:1, end: 5}, {start: 22, end: 100}]"    
    >
</CodeBlock>


### Full Payload Example

Below is a full sample of the payload.  The `meta_data` is just an example and can be formatted with any valid JSON or a simple value for a text block. 
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/payloads/payload_sample.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/payloads/payload_sample.json"
    lang="json"
    >
</CodeBlock>


## Example with 🐍 Python

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/aplos_nca/main.py"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/python/aplos_nca/main.py"
    lang="python"    
    :displayLines="[{start:1, end: 21}, {start: 92, end: 143}]"    
    >
</CodeBlock>

