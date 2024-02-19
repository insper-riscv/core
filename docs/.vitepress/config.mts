import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "CTI Renato Archer - RISC-V",
  description: "Documentação do Projeto",
  base: '/24a-CTI-RISCV/',
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Project', link: '/project' }
    ],

    sidebar: [
      {
        text: 'Project',
        items: [
          { text: 'Introduction', link: '/project' },
          { text: 'RISC-V Processor', link: '/diagram' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/pfeinsper/24a-CTI-RISCV' }
    ]
  }
})
