import { defineConfig } from 'vitepress'
import apiSidebar from '../sidebar_navs/api.json'
import methodsSidebar from '../sidebar_navs/methods.json'
import quickstartSidebar from '../sidebar_navs/quickstart.json'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Aplos NCA Documentation",
  description: "Aploc NCA Documentation for the NCA Engine",
  head: [
    ['link', { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  ],
  srcExclude: ['**/README.md', '**/readme.md', '**/TODO.md', '**/todo.md'],
  themeConfig: {
    
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Quick Start', link: '/docs/quickstart/aplosnca'},
      { text: 'API Reference', link: '/docs/api/index' },
      { text: 'Documentation', link: '/docs/methods/index' }

    ],
    
    sidebar: {
      ...quickstartSidebar,
      ...apiSidebar,
      ...methodsSidebar
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
    
  },
  
})
