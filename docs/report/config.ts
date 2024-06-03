import { type DefaultTheme } from 'vitepress'


export const sidebar : DefaultTheme.Sidebar = {
  '/report/': [
    {
      text: '♺ Imprimir',
      link: 'javascript:print()',
      target: '_top',
    }, {
      text: 'Documentos',
      items: [
        {
          text: 'Relatório',
          link: '/report/',
        }, {
          text: 'Apêndice A',
          link: '/report/appendix-a/',
        }, {
          text: 'Anexo A',
          link: '/report/attachment-a/',
        },
      ],
    },
  ],
}
