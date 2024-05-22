<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import { VPDocAsideSponsors } from 'vitepress/theme'

const sponsors = [
    {
        size: 'mini',
        items: [
            {
                name: 'Centro de Tecnologia da Informação Renato Archer',
                img: '/24a-CTI-RISCV/images/logo_cti_renato_archer.png',
                url: 'https://www.gov.br/cti/pt-br',
            }, {
                name: 'Projeto Final de Engenharia Insper',
                img: '/24a-CTI-RISCV/images/logo-insper-positivo.png',
                url: 'https://www.insper.edu.br/pfe/',
            },
        ],
    },
]

</script>

<template>
  <DefaultTheme.Layout>
    <template #aside-ads-after>
        <VPDocAsideSponsors :data="sponsors"/>
    </template>
  </DefaultTheme.Layout>
</template>
