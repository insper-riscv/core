import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/en/guia/': [
            {
                text: 'About',
                link: '/guia/',
            }, {
                text: 'Introduction',
                link: '/guia/introducao'
            }, {
                text: 'Development',
                link: '/guia/desenvolvimento'
            }, {
                text: 'Bibliography',
                link: '/guia/bibliografia'
            },
        ],
    },
} satisfies DefaultTheme.Config
