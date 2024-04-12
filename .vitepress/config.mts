import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Aplos NCA Documentation",
  description: "Aploc NCA Documentation for the NCA Engine",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Aplos API', link: '/docs/api/index' },
      { text: 'Aplos Methods', link: '/docs/methods/index' }

    ],

    
    sidebar: {
      '/docs/api/': [
        {
          text: 'Executions',
          items: [
            { text: '1. Run', link: '/docs/api/executions/1.Run' },
            { text: '2. Status', link: '/docs/api/executions/2.Status' },
            { text: '3. List', link: '/docs/api/executions/3.List' },
            
          ]
        },
        {
          text: 'Tenants',
          items: [
            { text: '1. Get Tenant', link: '/docs/api/tenants/1.GetTenant' },
            { text: '2. Get Subscriptio ', link: '/docs/api/tenants/2.GetSubscription' },
            
            
          ]
        },
        {
          text: 'Users',
          items: [
            { text: '1. Create User', link: '/docs/api/users/1.CreateUser' },
            { text: '2. List Users', link: '/docs/api/users/2.ListUsers' },
            { text: '3. Update User', link: '/docs/api/users/3.UpdateUser' },
            { text: '3. Update User Status', link: '/docs/api/users/4.UpdateUserStatus' },
            { text: '3. Update User Password', link: '/docs/api/users/5.UpdatePassword' },
            
          ]
        }
      ],
        '/docs/methods/': [ {
          text: 'Methods',
          items: [
            { text: 'AUC Methods', link: '/docs/methods/aucmethods' },
            { text: 'AUMC Methods', link: '/docs/methods/aumcmethods' },
            { text: 'Extrapolation Methods', link: '/docs/methods/extrapolationmethods' },
            { text: 'Terminal Slope', link: '/docs/methods/terminalslope' }
          ]

        },
        {
          text: 'IV',
          items: [
            { text: 'Markdown Examples', link: '/markdown-examples' },
            { text: 'Runtime API Examples', link: '/api-examples' }
          ]

        },
        {
          text: 'EV',
          items: [
            { text: 'Extravascular Single Dose', link: '/docs/methods/ExtravascularSingleDose' },
            { text: 'Extravascular Steady State', link: '/docs/methods/ExtravascularSteadyState' }
          ]

        }
        
      ]
    },
    search: {
      provider: 'local'
    },
    
    socialLinks: [
      { icon: 'linkedin', link: 'https://www.linkedin.com/company/aplos-analytics/' }
    ]
  }
})
