---
layout: home
hero:
  name: RISC-V para uso Aeroespacial
  text: Documentação do Projeto
  tagline: CTI Renato Archer e PFE Insper
  actions:
    - theme: brand
      text: Projeto
      link: /project
---

<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [
  {
    avatar: 'https://media.licdn.com/dms/image/C4E03AQEpCgpnDSn1Rg/profile-displayphoto-shrink_400_400/0/1617900258233?e=1714003200&v=beta&t=3E9dMYeFAvXG_k_Ktv9598Qnim9UO1141zZQCum2mGI',
    name: 'Giancarlo Ruggiero',
    title: 'Developer',
    links: [
      { icon: 'github', link: 'https://github.com/gianvr' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/giancarlo-vr/' }
    ]
  }, 
  {
    avatar: 'https://media.licdn.com/dms/image/D4D03AQGHydd8FnBOdA/profile-displayphoto-shrink_400_400/0/1707877218390?e=1714003200&v=beta&t=OqbtDvw0qaaZ7Lx7iykHOWjNEAe5KISyyJstXY6Omjk',
    name: 'Luciano Felix',
    title: 'Developer',
    links: [
      { icon: 'github', link: 'https://github.com/FelixLuciano' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/luciano-felix/' }
    ]
  },
  {
    avatar: 'https://media.licdn.com/dms/image/D4E03AQFt5YSf5FbxKg/profile-displayphoto-shrink_200_200/0/1666467108985?e=2147483647&v=beta&t=b0XQGht56s_SqQ4i46sv17sWOQ9g3Bbtv8yh1XFbKtg',
    name: 'Tiago Seixas',
    title: 'Developer',
    links: [
      { icon: 'github', link: 'https://github.com/TiagoSeixas2103' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/tiago-seixas-bb9614254/' }
    ]
  },
  {
    avatar: 'https://media.licdn.com/dms/image/C5103AQEOCjELDx5ajA/profile-displayphoto-shrink_800_800/0/1517465490173?e=1714003200&v=beta&t=8ZRnaxdyEzryRQViqNk6_-B4G72lMULu5xFGh4tfId8',
    name: 'Rafael Corsi',
    title: 'Professor',
    links: [
      { icon: 'github', link: 'https://github.com/rafaelcorsi' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/rafael-corsi-ferrão-624238116/' }
    ]
  }
]
</script>

<VPTeamMembers size="small" :members="members" />



