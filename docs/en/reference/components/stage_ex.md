---
outline: 2
---

# EX - Executa

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/STAGE_EX.vhd" target="blank" style="float:right"><Badge type="tip" text="STAGE_EX.vhd &boxbox;" /></a>

<<< @/../src/TOP_LEVEL.vhd{vhdl:line-numbers}

:::

## Topology

```mermaid
%%{ init: { 'flowchart': { 'curve': 'step' } } }%%
flowchart LR
    subgraph TOP[STAGE_EX]
        direction LR

        STATE[("<span style="padding:8em 0;writing-mode:vertical-lr">Registrador de pipeline</span>")]

        subgraph GENERIC ["generic map"]
            direction LR
            GENERATE_REGISTERS
        end

        subgraph G_EXU_CTRL[Execution Unit Controller]
            direction LR
            EXU_CTRL(\n\nControlador da\nUnidade de\nExecução\n\n\n)
            click EXU_CTRL href "./module_control_unit.html"
        end

        subgraph G_EXU[Execution Unit]
            direction LR
            N[DATA_WIDTH]
            EXU(\n\nUnidade de\nExecução\n\n\n)
            click P href "./module_register_file.html"
        end

        STATE ===> EXU_CTRL & EXU
        EXU_CTRL -.-> EXU
        Q[XLEN] -.-> N
    end

    A((clock)) ----> TOP
    B(clear) ----> TOP
    C(enable) ----> TOP

    E[[source\n$.control_ex\n$.control_mem\n$.control_wb\n$.address_program\n$.data_source_1\n$.data_source_2\n$.data_immediate\n$.funct_7\n$.funct_3\n$.opcode\n$.select_destination]] ==> STATE
    STATE & EXU ==> J[[destination\n$.control_mem\n$.control_wb\n$.address_pointer\n$.data_source_2\n$.select_destination]]
```

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

![RTL view from Decodifica Instrução](/images/reference/components/stage_ex_netlist.svg){.w-full .dark-invert}

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_STAGE_EX.py" target="blank" style="float:right"><Badge type="tip" text="test_STAGE_EX.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Case 1 <Badge type="info" text="tb_stage_ex_case_1" />

Waveform:

![Waveform from caso de teste 1 do Decodifica Instrução](/images/reference/components/tb_stage_ex_case_1.svg){.w-full .dark-invert}
```

:::
