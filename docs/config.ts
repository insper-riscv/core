import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  description: 'Project Documentation',

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      {
        text: 'Guia',
        link: '/guide/',
        activeMatch: '/reference/'
      }, {
        text: 'Referência',
        link: '/reference/components/',
      }, {
        text: 'Mais',
        items: [
          {
            text: 'Sobre',
            link: '/guide/',
          }, {
            text: 'Bibliografia',
            link: '/guide/bibliography'
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

    search: {
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: "Pesquisar",
                buttonAriaLabel: "Pesquisar"
              },
              modal: {
                displayDetails: "Exibição detalhada",
                resetButtonTitle: "Limpar pesquisa",
                noResultsText: "Não há resultados para",
                backButtonTitle: "Voltar",
                footer: {
                  closeText: "Fechar",
                  navigateText: "Navegação",
                  selectText: "Selecionar",
                }
              }
            }
          }
        }
      }
    },

    sidebar: {
      ...require('./guide/config.ts').default.sidebar,
      ...require('./reference/config.ts').default.sidebar,
    },

    outline: 'deep',
    outlineTitle: 'Tópicos',

    editLink: {
      pattern: 'https://github.com/pfeinsper/24a-CTI-RISCV/edit/docs/docs/:path',
      text: 'Editar esta página'
    },

    lastUpdated: {
      text: 'Última modificação em',
      formatOptions: {
        dateStyle: 'long',
        timeStyle: 'short'
      }
    },

    docFooter: {
      prev: 'Página anterior',
      next: 'Próxima página'
    },

    darkModeSwitchLabel: 'Aparência',
    returnToTopLabel: 'Voltar para o topo',
    langMenuLabel: 'Mudar idioma',
  
    footer: {
      message: 'Publicado sob a Licença MIT.',
      copyright: 'Copyright © 2024'
    },
  },
})
