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
|The Analysis File|via where it is in S3|
|The Configuration|supplied in JSON format|
|Meta Data|Optional: Supplied in JSON format or text.  This is stored "as-is" in the record and you can use to as you see fit.  Example uses: Tracking id's for internal use.  Tagging Team members etc.|


## Example with 🐍 Python

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/aplos_nca/main.py"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/python/aplos_nca/main.py"
    lang="python"    
    :displayLines="[{start:1, end: 21}, {start: 92, end: 143}]"    
    >
</CodeBlock>

