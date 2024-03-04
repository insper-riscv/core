import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/guia/': [
            {
                text: 'Documentação',
                items: [
                    { text: 'Introdução', link: '/guia/introducao' },
                    { text: 'Desenvolvimento', link: '/guia/desenvolvimento' },
                    { text: 'RISC-V', link: '/guia/diagrama' }
                ],
            }
        ],
    },
} satisfies DefaultTheme.Config
