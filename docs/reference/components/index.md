---
outline: 2
---

# Top Level

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/TOP_LEVEL.vhd" target="blank" style="float:right"><Badge type="tip" text="TOP_LEVEL.vhd &boxbox;" /></a>

<<< @/../src/TOP_LEVEL.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container>

![Topologia do Top Level](/images/reference/components/top_level_core.drawio.svg){.w-full .dark-invert}

</pan-container>

## Diagrama de Fluxo de Dados

### Diagrama simplificado

<pan-container>

![](/images/reference/components/top_level_pipeline.drawio.svg){.w-full .dark-invert}

</pan-container>

### Diagrama detalhado

<pan-container selector=".mermaid">

<!--@include: @/.includes/top_level-topology.md-->

</pan-container>

## Usagem

::: danger TO DO

Work in progress.

:::

## Diagrama RTL

<pan-container>

![Diagrama de RTL do Top Level](/images/reference/components/top_level_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_TOP_LEVEL.py" target="blank" style="float:right"><Badge type="tip" text="test_TOP_LEVEL.py &boxbox;" /></a>

<<< @/../test/test_TOP_LEVEL.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_top_level_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do Top Level](/images/reference/components/tb_top_level_case_1.svg){.w-full .dark-invert}

</pan-container>
