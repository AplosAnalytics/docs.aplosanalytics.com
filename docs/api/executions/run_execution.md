<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# 🚀 Run an Analysis on the NCA Engine

Once a file is uploaded you can run an NCA Engine Execution against it.  

In general, you can follow the flow of:
1. Uploading a file 
2. Then run an execute action right away

Or 
1. Upload one or more files
2. Run executions at a later date and time. see [Listing Files](../users/list-files.md)

> [!TIP]
> No matter which flow you take,  the execution portion is the same and in this section, we'll take a deeper dive into how to run an execution.

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

Below is a sample of the payload required for submission.  For this quick introduction to the `payload` we'll skip all the details and only show the 3 parts, including the optional `"meta_data"`.
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/payloads/payload_sample.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/payloads/payload_sample.json"
    lang="json"    
    :displayLines="[{start:1, end: 5}, 6, 21, 22, 71, 72, 73 ]"    
    >
</CodeBlock>


### Full Payload Example

Below is a full sample of the payload.  The `meta_data` is just an example and can be formatted with any valid JSON or a simple value for a text block. 

As you can see the `meta_data` can be useful for storing additional data along with your analysis.

The `configuration` includes the necessary parameters that are required to run your analysis.

> [!TIP]
> For now you don't need to know the details of the configuration file.  We have fully functioning samples to help you get started.



<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/payloads/payload_sample.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/payloads/payload_sample.json"
    lang="json"
    :highlightLines=[2,6,22]
    >
</CodeBlock>


## Response

The response will come back with an `execution_id` and a `status`.  Use execution_id to get status updates.
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/run_execution_response.json"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/run_execution_response.json"
    lang="json"    
    >
</CodeBlock>


## Example with 🐍 Python

Example of how an execution is launched.

<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/aplos_nca/main.py"    
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/python/aplos_nca/main.py"
    lang="python"    
    :displayLines="[{start: 92, end: 143}]"
    >
</CodeBlock>

