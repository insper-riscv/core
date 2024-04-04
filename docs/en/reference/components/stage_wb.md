---
outline: 2
---

# WB - Escreve o Retorno

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/STAGE_WB.vhd" target="blank" style="float:right"><Badge type="tip" text="STAGE_WB.vhd &boxbox;" /></a>

<<< @/../src/TOP_LEVEL.vhd{vhdl:line-numbers}

:::

## Topology

![Topologia do Escreve o Retorno](/images/reference/components/stage_wb.drawio.svg){.w-full .dark-invert}

## Generic interface

### `GENERATE_REGISTERS` <Badge type="tip" text="GENERIC" />

Define geração de registradores de pipeline.

- Type: `boolean `
- Default: `TRUE`

## Port interface

### `clock` <Badge type="warning" text="INPUT" />

Entrada do sinal de clock.

- Type: `std_logic`

::: danger TO DO

Work in progress.

:::

## Usage

::: danger TO DO

Work in progress.

:::

## RTL View

![RTL view from Escreve o Retorno](/images/reference/components/stage_wb_netlist.svg){.w-full .dark-invert}

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_STAGE_WB.py" target="blank" style="float:right"><Badge type="tip" text="test_STAGE_WB.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Case 1 <Badge type="info" text="tb_stage_wb_case_1" />

Waveform:

![Waveform from caso de teste 1 do Escreve o Retorno](/images/reference/components/tb_stage_wb_case_1.svg){.w-full .dark-invert}
```

:::
