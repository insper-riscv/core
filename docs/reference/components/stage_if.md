---
outline: 2
---

# IF - Busca Instrução

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/STAGE_IF.vhd" target="blank" style="float:right"><Badge type="tip" text="STAGE_IF.vhd &boxbox;" /></a>

<<< @/../src/STAGE_IF.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

<!--@include: @/.includes/stage_if-topology.md-->

</pan-container>

## Interface de portas

### `clock` <Badge type="success" text="INPUT" />

Entrada do sinal de clock.

- Tipo: `std_logic`

::: danger TO DO

Work in progress.

:::

## Usagem

::: danger TO DO

Work in progress.

:::

## Diagrama RTL

<pan-container>

![Diagrama de RTL do Busca Instrução](/images/reference/components/stage_if_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_STAGE_IF.py" target="blank" style="float:right"><Badge type="tip" text="test_STAGE_IF.py &boxbox;" /></a>

<<< @/../test/test_STAGE_IF.py{py:line-numbers}

:::

::: danger TO DO

```md
### Caso 1 <Badge type="info" text="tb_stage_if_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do Busca Instrução](/images/reference/components/tb_stage_if_case_1.svg){.w-full .dark-invert}

</pan-container>

```

:::