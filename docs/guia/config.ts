import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/guia/': [
            {
                text: 'Sobre',
                link: '/guia/',
            }, {
                text: 'Introdução',
                link: '/guia/introducao'
            }, {
                text: 'Desenvolvimento',
                link: '/guia/desenvolvimento'
            }, {
                text: 'Bibliografia',
                link: '/guia/bibliografia'
            },
        ],
    },
} satisfies DefaultTheme.Config
