---
outline: 2
---

# Unidade de Execução

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/MODULE_EXECUTION_UNIT.vhd" target="blank" style="float:right"><Badge type="tip" text="MODULE_EXECUTION_UNIT.vhd &boxbox;" /></a>

<<< @/../src/MODULE_ALU.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container>

<!--@include: @/.includes/module_execution_unit-topology.md-->

</pan-container>

## Interface genérica

::: danger TO DO

Work in progress.

:::

## Interface de portas

::: danger TO DO

Diagrama a nível de registradores

:::

## Usagem

::: danger TO DO

Work in progress.

:::

## Diagrama RTL

<pan-container>

![Diagrama de RTL da Unidade de Execução](/images/reference/components/module_alu_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_MODULE_EXECUTION_UNIT.py" target="blank" style="float:right"><Badge type="tip" text="test_MODULE_EXECUTION_UNIT.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Caso 1 <Badge type="info" text="tb_module_execution_unit_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 da Controlador da Unidade de Execução/images/reference/components/tb_module_execution_unit_case_1.svg){.w-full .dark-invert}

</pan-container>

```

:::