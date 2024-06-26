import { defineConfig } from 'vitepress'
import apiSidebar from '../sidebar_navs/api.json'
import methodsSidebar from '../sidebar_navs/methods.json'
import quickstartSidebar from '../sidebar_navs/quickstart.json'
import samplesSidebar from '../sidebar_navs/samples.json'
import MarkdownIt from 'markdown-it'
import markdownItGithubAlerts from 'markdown-it-github-alerts'


// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Aplos NCA Docs",
  description: "Documentation for the Aplos NCA Engine",
  head: [
    ['link', { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  ],
  srcExclude: ['**/README.md', '**/readme.md', '**/TODO.md', '**/todo.md'],
  themeConfig: {
    logo: '/logomark_fullcolor.svg',
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Quick Start', link: '/docs/quickstart/aplosnca'},
      { text: 'API Reference', link: '/docs/api/index' },
      { text: 'Documentation', link: '/docs/methods/index' },
      { text: 'Examples', link: '/docs/samples/index' }

    ],
    sidebar: {
      ...quickstartSidebar,
      ...apiSidebar,
      ...methodsSidebar,
      ...samplesSidebar
    },
    footer: {
      copyright: 'Copyright &copy; 2023-Present Aplos Analytics, Inc.'
    },
    search: {
      provider: 'local'
    },
    socialLinks: [
      { icon: 'linkedin', link: 'https://www.linkedin.com/company/aplos-analytics/' }
    ]
  },
  markdown: {
    math: true,  // Enable built-in math support,
    config: (md) => {
      md.use(markdownItGithubAlerts)
    }
  },
  
})
