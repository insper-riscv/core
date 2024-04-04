---
outline: 2
---

# ID - Decodifica Instrução

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/STAGE_ID.vhd" target="blank" style="float:right"><Badge type="tip" text="STAGE_ID.vhd &boxbox;" /></a>

<<< @/../src/TOP_LEVEL.vhd{vhdl:line-numbers}

:::

## Topology

```mermaid
%%{ init: { 'flowchart': { 'curve': 'step' } } }%%
flowchart LR
    subgraph TOP[STAGE_ID]
        direction LR

        subgraph GENERIC ["generic map"]
            direction LR
            GENERATE_REGISTERS
        end

        STATE[("<span style="padding:8em 0;writing-mode:vertical-lr">Registrador de pipeline</span>")]

        subgraph CU[Control Unit]
            direction LR
            K[DATA_WIDTH]
            L(\n\nUnidade de\nControle\n\n\n)
            click L href "./module_control_unit.html"
        end

        subgraph RF[Arquivo de\nRegistradores]
            direction LR
            N[DATA_WIDTH]
            O[ADDRESS_WIDTH]
            P(\n\nUnidade de\nControle\n\n\n)
            click P href "./module_register_file.html"
        end

        STATE ===> CU & RF
        M[XLEN] -.-> K
        Q[XLEN] -.-> N
        R[5] -.-> O
    end
    
    C(enable) ----> TOP
    B(clear) ----> TOP
    A((clock)) ----> TOP
    D(enable_destination) --> STATE
    F(select_destination) --> STATE
    G(data_destination) --> STATE

    E[[source\n$.address_program\n$.data_instruction]] ==> STATE
    CU --> H(address_jump)
    CU --> I[[control_if\n$.enable_stall\n$.enable_flush\n$.enable_jump\n$.select_source]]
    RF & CU --> J[[signals_ex\n$.control_ex\n$.control_mem\n$.control_wb\n$.address_program\n$.data_source_1\n$.data_source_2\n$.data_immediate\n$.funct_7\n$.funct_3\n$.opcode\n$.select_destination]]
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

![RTL view from Decodifica Instrução](/images/reference/components/stage_id_netlist.svg){.w-full .dark-invert}

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_STAGE_ID.py" target="blank" style="float:right"><Badge type="tip" text="test_STAGE_ID.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Case 1 <Badge type="info" text="tb_stage_id_case_1" />

Waveform:

![Waveform from caso de teste 1 do Decodifica Instrução](/images/reference/components/tb_stage_id_case_1.svg){.w-full .dark-invert}
```

:::
