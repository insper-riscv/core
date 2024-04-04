import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  description: 'Project Documentation',

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      {
        text: 'Guide',
        link: '/en/guide/',
      }, {
        text: 'Reference',
        link: '/en/reference/components/',
      }, {
        text: 'More',
        items: [
          {
            text: 'About',
            link: '/en/guide/',
          }, {
            text: 'Bibliography',
            link: '/en/guide/bibliography'
          }, {
            text: 'CTI Renato Archer',
            link: 'https://www.gov.br/cti/pt-br'
          }, {
            text: 'PFE Insper',
            link: 'https://www.insper.edu.br/pfe/'
          }
        ],
      },
    ],

    sidebar: {
      ...require('../en/guide/config.ts').default.sidebar,
      ...require('../en/reference/config.ts').default.sidebar,
    },

    outline: 'deep',
    outlineTitle: 'Topics',

    editLink: {
      pattern: 'https://github.com/pfeinsper/24a-CTI-RISCV/edit/docs/docs/:path',
      text: 'Edit this page'
    },

    lastUpdated: {
      text: 'Last modified at',
      formatOptions: {
        dateStyle: 'long',
        timeStyle: 'short'
      }
    },

    docFooter: {
      prev: 'Previous page',
      next: 'Next page'
    },

    darkModeSwitchLabel: 'Appearence',
    returnToTopLabel: 'Back to top',
    langMenuLabel: 'Change language',
  
    footer: {
      message: 'Published under the MIT License.',
      copyright: 'Copyright © 2024'
    },
  },
})
