# read me


## Setup

### Commands 
```shell
# install packages
npm install   
# build the output
npm run build 
```

### Output
1. Creates a `.vitepress\dist` directory

### Deployment
When deploying the site, you can copy the output to the s3 bucket (or wherever it's hosted)
1. Copy the `dist` directory to the cdn



## Local Execution
You can run the code locally by running the following command.

```shell
npm run dev
```

This should do hot loading, meaning that any changes you make to the code, should be automatically updated and rendered.



### Side Bar Navigation
The sidebar navigation is controlled in the `.vitepress/config.mts` file
Currently, we have two array elements that control the sidebar navigation based on the path of the docs:

```javascript

sidebar: {
      '/docs/api/': {
          text: '<heading>',
          items: [
            { text: '<Title of line>', link: '<full-path-to-link>'}
            
          ]
        },
        '/docs/methods/': {
          text: '<heading>',
          items: [
            { text: '<Title of line>', link: '<full-path-to-link>'}
            
          ]
        },
        ... more if needed


```


## Code snippets

Add the following to the top of your `.md` file to embed a code snippet that exists elsewhere.
```html
<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>
```

Then include the block like the following.

- `src`: The full URL to the code you want to include. Use the `raw` version
- `lang`: the language you want to be formatted

```html
<CodeBlock src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/shell/amazon-cognito-jwt.sh" lang="shell"></CodeBlock>
```

## ToDo's
- Line Numbering
- Specific Line Numbers: only output specific line numbers based on a range.