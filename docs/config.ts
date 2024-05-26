import { defineConfig, type DefaultTheme } from 'vitepress'

import { sidebar as guideSidebar } from './guide/config'
import { sidebar as referenceSidebar } from './reference/config'
import { sidebar as reportSidebar } from './report/config'

// https://vitepress.dev/reference/site-config
export const pt = defineConfig({
  description: 'Documentação do Projeto',

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      {
        text: 'Guia',
        link: '/guide/',
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
            text: 'Começando',
            link: '/guide/',
          }, {
            text: 'Organização',
            link: '/reference/components/',
          }, {
            text: 'Especificação',
            link: '/reference/components/',
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

    sidebar: {
      ...guideSidebar,
      ...referenceSidebar,
      ...reportSidebar,
    },

    editLink: {
      pattern: 'https://github.com/pfeinsper/24a-CTI-RISCV/edit/docs/docs/:path',
      text: 'Edite esta página no GitHub'
    },

    docFooter: {
      prev: 'Anterior',
      next: 'Próximo'
    },

    outline: 'deep',
    outlineTitle: 'Tópicos',

    lastUpdated: {
      text: 'Atualizado em',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'medium'
      }
    },

    langMenuLabel: 'Alterar Idioma',
    returnToTopLabel: 'Voltar ao Topo',
    sidebarMenuLabel: 'Menu Lateral',
    darkModeSwitchLabel: 'Tema Escuro',
    lightModeSwitchTitle: 'Mudar para Modo Claro',
    darkModeSwitchTitle: 'Mudar para Modo Escuro',
  
    footer: {
      message: 'Publicado sob a Licença MIT.',
      copyright: 'Copyright © 2024',
    },
  },
})

export const search: DefaultTheme.AlgoliaSearchOptions['locales'] = {
  pt: {
    placeholder: 'Pesquisar documentos',
    translations: {
      button: {
        buttonText: 'Pesquisar',
        buttonAriaLabel: 'Pesquisar'
      },
      modal: {
        searchBox: {
          resetButtonTitle: 'Limpar pesquisa',
          resetButtonAriaLabel: 'Limpar pesquisa',
          cancelButtonText: 'Cancelar',
          cancelButtonAriaLabel: 'Cancelar',
        },
        startScreen: {
          recentSearchesTitle: 'Histórico de Pesquisa',
          noRecentSearchesText: 'Nenhuma pesquisa recente',
          saveRecentSearchButtonTitle: 'Salvar no histórico de pesquisas',
          removeRecentSearchButtonTitle: 'Remover do histórico de pesquisas',
          favoriteSearchesTitle: 'Favoritos',
          removeFavoriteSearchButtonTitle: 'Remover dos favoritos',
        },
        errorScreen: {
          titleText: 'Não foi possível obter resultados',
          helpText: 'Verifique a sua conexão de rede',
        },
        footer: {
          selectText: 'Selecionar',
          navigateText: 'Navegar',
          closeText: 'Fechar',
          searchByText: 'Pesquisa por',
        },
        noResultsScreen: {
          noResultsText: 'Não foi possível encontrar resultados',
          suggestedQueryText: 'Você pode tentar uma nova consulta',
          reportMissingResultsText: 'Deveriam haver resultados para essa consulta?',
          reportMissingResultsLinkText: 'Clique para enviar feedback',
        },
      },
    },
  },
}
