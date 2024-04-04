---
outline: 2
---

# MEM - Acessa a Memória

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/STAGE_MEM.vhd" target="blank" style="float:right"><Badge type="tip" text="STAGE_MEM.vhd &boxbox;" /></a>

<<< @/../src/TOP_LEVEL.vhd{vhdl:line-numbers}

:::

## Topology

![Topologia do Acessa a Memória](/images/reference/components/stage_mem.drawio.svg){.w-full .dark-invert}

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

![RTL view from Decodifica Instrução](/images/reference/components/stage_mem_netlist.svg){.w-full .dark-invert}

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_STAGE_MEM.py" target="blank" style="float:right"><Badge type="tip" text="test_STAGE_MEM.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Case 1 <Badge type="info" text="tb_stage_mem_case_1" />

Waveform:

![Waveform from caso de teste 1 do Decodifica Instrução](/images/reference/components/tb_stage_mem_case_1.svg){.w-full .dark-invert}
```

:::
