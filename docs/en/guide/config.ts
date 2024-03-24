import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/en/guide/': [
            {
                text: 'About',
                link: '/en/guide/',
            }, {
                text: 'Introduction',
                link: '/en/guide/introducao'
            }, {
                text: 'Development',
                link: '/en/guide/desenvolvimento'
            }, {
                text: 'Bibliography',
                link: '/en/guide/bibliografia'
            },
        ],
    },
} satisfies DefaultTheme.Config
