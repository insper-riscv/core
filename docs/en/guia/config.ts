import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/en/guia/': [
            {
                text: 'About',
                link: '/en/guia/',
            }, {
                text: 'Introduction',
                link: '/en/guia/introducao'
            }, {
                text: 'Development',
                link: '/en/guia/desenvolvimento'
            }, {
                text: 'Bibliography',
                link: '/en/guia/bibliografia'
            },
        ],
    },
} satisfies DefaultTheme.Config
