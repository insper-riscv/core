---
outline: 2
---

# Bit da ULA

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/RV32I_ALU_BIT.vhd" target="blank" style="float:right"><Badge type="tip" text="RV32I_ALU_BIT.vhd &boxbox;" /></a>

<<< @/../src/RV32I_ALU_BIT.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container>

<!--@include: @/.includes/rv32i_alu_bit-topology.md-->

</pan-container>

## Interface genérica

::: danger TO DO

Work in progress.

:::

## Interface de portas

::: danger TO DO

Work in progress.

:::

## Diagrama RTL

<pan-container>

![Diagrama de RTL do bit da ULA](/images/reference/components/rv32i_alu_bit_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_RV32I_ALU_BIT.py" target="blank" style="float:right"><Badge type="tip" text="test_RV32I_ALU_BIT.py &boxbox;" /></a>

<<< @/../test/test_RV32I_ALU_BIT.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_rv32i_alu_bit_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do Bit da ULA](/images/reference/components/tb_rv32i_alu_bit_case_1.svg){.w-full .dark-invert}

</pan-container>