<script setup>
import { VPTeamMembers } from 'vitepress/theme'
</script>


<!--@include: @/report/resumo.md-->

<script>
const a = {
  members24_1: [
    {
      avatar: "https://media.licdn.com/dms/image/C5103AQEOCjELDx5ajA/profile-displayphoto-shrink_800_800/0/1517465490173?e=1714003200&v=beta&t=8ZRnaxdyEzryRQViqNk6_-B4G72lMULu5xFGh4tfId8",
      name: "Rafael Corsi",
      title: "Orientador",
      links: [
        {
          icon: "linkedin",
          link: "https://www.linkedin.com/in/rafael-corsi-ferrão-624238116/"
        }, {
          icon: "github",
          link: "https://github.com/rafaelcorsi"
        }
      ]
    }, {
      avatar: "https://media.licdn.com/dms/image/C4E03AQEpCgpnDSn1Rg/profile-displayphoto-shrink_400_400/0/1617900258233?e=1714003200&v=beta&t=3E9dMYeFAvXG_k_Ktv9598Qnim9UO1141zZQCum2mGI",
      name: "Giancarlo Ruggiero",
      title: "Desenvolvedor",
      links: [
        {
          icon: "linkedin",
          link: "https://www.linkedin.com/in/giancarlo-vr/"
        }, {
          icon: "github",
          link: "https://github.com/gianvr"
        }
      ]
    }, {
      avatar: "https://media.licdn.com/dms/image/D4D03AQGHydd8FnBOdA/profile-displayphoto-shrink_400_400/0/1707877218390?e=1714003200&v=beta&t=OqbtDvw0qaaZ7Lx7iykHOWjNEAe5KISyyJstXY6Omjk",
      name: "Luciano Felix",
      title: "Desenvolvedor",
      links: [
        {
          icon: "linkedin",
          link: "https://www.linkedin.com/in/luciano-felix/"
        }, {
          icon: "github",
          link: "https://github.com/FelixLuciano"
        }
      ]
    }, {
      avatar: "https://media.licdn.com/dms/image/D4E03AQFt5YSf5FbxKg/profile-displayphoto-shrink_200_200/0/1666467108985?e=2147483647&v=beta&t=b0XQGht56s_SqQ4i46sv17sWOQ9g3Bbtv8yh1XFbKtg",
      name: "Tiago Seixas",
      title: "Desenvolvedor",
      links: [
        {
          icon: "linkedin",
          link: "https://www.linkedin.com/in/tiago-seixas-bb9614254/"
        }, {
          icon: "github",
          link: "https://github.com/TiagoSeixas2103"
        }
      ]
    },
  ],
  org: [
    {
      avatar: "https://media.licdn.com/dms/image/C4D0BAQF6iPH2r0sRCA/company-logo_200_200/0/1630470864507/cti_renato_archer_logo?e=1716422400&v=beta&t=IXE8hu6bInWiNoIVn--Z6Cm4Hd-5ywIkS6h6Txvzb0w",
      name: "CTI Renato Archer",
      title: "Realização",
      links: [
        {
          icon: "linkedin",
          link: "https://www.linkedin.com/company/cti-renato-archer/"
        }
      ]
    }, {
      avatar: "https://media.licdn.com/dms/image/D4E03AQG3diHhspG70w/profile-displayphoto-shrink_800_800/0/1665021953301?e=1714003200&v=beta&t=4G8s6U3TEc9sP6ziTJSFfIQnScdIDrYayt5sHjwIij8",
      name: "Saulo Finco",
      title: "Mentor",
      links: [
        {
          icon: "linkedin",
          link: "https://www.linkedin.com/in/saulofinco"
        }
      ]
    }
  ],
}
</script>

## Organização

<VPTeamMembers :members="a.org" />

## Equipe PFE 2024.1

<VPTeamMembers :members="a.members24_1" />
