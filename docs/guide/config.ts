import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/guide/': [
            {
                text: 'Sobre',
                link: '/guide/',
            }, {
                text: 'Introdução',
                link: '/guide/introduction'
            }, {
                text: 'Começando',
                link: '/guide/getting-started'
            }, {
                text: 'Desenvolvimento',
                link: '/guide/desenvolvimento'
            }, {
                text: 'Bibliografia',
                link: '/guide/bibliography'
            },
        ],
    },
} satisfies DefaultTheme.Config
