---
outline: 2
---

# EX - Executa

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/STAGE_EX.vhd" target="blank" style="float:right"><Badge type="tip" text="STAGE_EX.vhd &boxbox;" /></a>

<<< @/../src/STAGE_EX.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

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

</pan-container>

## Interface genérica

### `GENERATE_REGISTERS` <Badge type="neutral" text="GENERIC" />

Define geração de registradores de pipeline.

- Tipo: `boolean `
- Padrão: `TRUE`

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

![Diagrama de RTL do Decodifica Instrução](/images/reference/components/stage_ex_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_STAGE_EX.py" target="blank" style="float:right"><Badge type="tip" text="test_STAGE_EX.py &boxbox;" /></a>

<<< @/../test/test_STAGE_EX.py{py:line-numbers}

:::

::: danger TO DO

```md
### Caso 1 <Badge type="info" text="tb_stage_ex_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do Decodifica Instrução](/images/reference/components/tb_stage_ex_case_1.svg){.w-full .dark-invert}

</pan-container>

```

:::
