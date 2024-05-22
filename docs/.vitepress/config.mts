import { defineConfig } from 'vitepress'
import mdItDeflist from 'markdown-it-deflist'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'RISC-V para uso Aeroespacial',
  description: 'Documentação do Projeto',
  base: '/24a-CTI-RISCV/',

  locales: {
    root: {
      label: 'Português',
      lang: 'pt'
    },
    en: {
      label: 'English (comming soon)'
    }
  },

  head: [
    ['link', { rel: 'icon', href: "/24a-CTI-RISCV/images/RISC-V_Stacked_Color.svg" }],
  ],

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      {
        text: 'Guia',
        link: '/guia/',
      }, {
        text: 'Referência',
        link: '/referencia/isa/',
      }, {
        text: 'Sobre',
        items: [
          {
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
      provider: 'local',
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
      ...require('../guia/config.ts').default.sidebar,
      ...require('../referencia/config.ts').default.sidebar,
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/pfeinsper/24a-CTI-RISCV' }
    ],

    outline: 'deep',
    outlineTitle: 'Tópicos',

    lastUpdatedText: 'Updated Date',

    docFooter: {
      prev: 'Página anterior',
      next: 'Próxima página'
    },

    darkModeSwitchLabel: 'Aparência',
    returnToTopLabel: 'Voltar para o topo',
    langMenuLabel: 'Mudar idioma',

    footer: {
      message: 'Publicado sob a Licença MIT.<br/>Icones por <a href="https://github.com/microsoft/fluentui-emoji">microsoft/fluentui-emoji</a>.',
      copyright: 'Copyright © 2024'
    },
  },

  markdown: {
    config(md) {
      md.use(mdItDeflist)
    },
  },
})
