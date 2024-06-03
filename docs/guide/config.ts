import { type DefaultTheme } from 'vitepress'


export const sidebar : DefaultTheme.Sidebar = {
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
}
