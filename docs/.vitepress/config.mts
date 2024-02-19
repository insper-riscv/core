import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "RISC-V para uso Aeroespacial",
  description: "Documentação do Projeto",
  base: '/24a-CTI-RISCV/',
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Docs', link: '/' },
      { text: 'CTI', link: 'https://www.gov.br/cti/pt-br' },
      { text: 'PFE Insper', link: 'https://www.insper.edu.br/pfe/' }
    ],

    sidebar: [
      {
        text: 'Projeto',
        items: [
          { text: 'Introdução', link: '/project' },
          { text: 'RISC-V', link: '/diagram' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/pfeinsper/24a-CTI-RISCV' }
    ]
  }
})
