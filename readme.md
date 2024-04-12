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
When deploying the site, you can copy the output to the s3 bucket (or whereever it's hosted)
1. Copy the `dist` directory to the cdn



## Local Execution
You can run the code locally by running the following command.

```shell
npm run dev
```

This should do hot loading, meaning that any changes you make to the code, should be automatically updated an rendered.



### Side Bar Naviation

The side bar navigation is controlled in the `.vitepress/config.mts` file

Currently we have two array elements which control the sidebar navigation based on the path of the docs:

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

