---
outline: 2
---

# Contador de Programa

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/MODULE_PROGRAM_COUNTER.vhd" target="blank" style="float:right"><Badge type="tip" text="MODULE_PROGRAM_COUNTER.vhd &boxbox;" /></a>

<<< @/../src/MODULE_PC.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container>

<!--@include: @/.includes/module_program_counter-topology.md-->

</pan-container>

## Interface genérica

::: danger TO DO

Work in progress.

:::

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

![Diagrama de RTL do Contador de Programa](/images/reference/components/module_program_counter_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_MODULE_PROGRAM_COUNTER.py" target="blank" style="float:right"><Badge type="tip" text="test_MODULE_PROGRAM_COUNTER.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Caso 1 <Badge type="info" text="tb_module_program_counter_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 da Controlador da Unidade de Execução/images/reference/components/tb_module_program_counter_case_1.svg){.w-full .dark-invert}

</pan-container>

```

:::
