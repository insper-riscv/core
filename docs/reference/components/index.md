---
outline: 2
---

# Top Level

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/TOP_LEVEL.vhd" target="blank" style="float:right"><Badge type="tip" text="TOP_LEVEL.vhd &boxbox;" /></a>

<<< @/../src/TOP_LEVEL.vhd{vhdl:line-numbers}

:::

## Topologia

![Topologia do Top Level](/images/reference/components/top_level_core.drawio.svg){.w-full .dark-invert}

## Diagrama de Fluxo de Dados

### Diagrama simplificado

![](/images/reference/components/top_level_pipeline.drawio.svg){.w-full .dark-invert}

### Diagrama detalhado

```mermaid
flowchart LR
    PC & ROM ==> IF/ID

    CU & RF -.-> ID/EX
    CU -.-> PC
    CU ===> PC
    ID/EX -.-> EX/MEM
    EX/MEM -.-> MEM/WB

    ALU ==> EX/MEM
    ID/EX ===> EX/MEM

    MEM ==> MEM/WB
    EX/MEM ==> MEM/WB

    subgraph STEP_WB ["Write Back"]
        MEM/WB[("<span style="padding:4em 0;writing-mode:vertical-lr">Registrador MEM/WB</span>")]
        WB((("Write\nBack")))
        MEM/WB -..-> WB
        MEM/WB ===> WB & WB
    end

    subgraph STEP_MEM ["Memory Access"]
        EX/MEM[("<span style="padding:4em 0;writing-mode:vertical-lr">Registrador EX/MEM</span>")]
        MEM[("\n\nMemory\n\n\n")]
        EX/MEM -..-> MEM
        EX/MEM ===> MEM
    end

    subgraph STEP_EX ["Execute"]
        ID/EX[("<span style="padding:4em 0;writing-mode:vertical-lr">Registrador ID/EX</span>")]
        ALU_CTRL[["Execution\nControl\nUnit"]]
        ALU{"Execution\nUnit"}
        ALU_CTRL -..-> ALU
        ID/EX -..-> ALU_CTRL
        ID/EX ==> ALU
    end

    subgraph STEP_ID ["Instruction Decode"]
        IF/ID[("<span style="padding:4em 0;writing-mode:vertical-lr">Registrador IF/ID</span>")]
        CU[["Control\nUnit"]]
        RF[("\n\nRegister\nFile\n\n\n")]
        CU -.-> RF
        RF ===> CU
        IF/ID ===> CU & RF
    end

    subgraph STEP_IF ["Instruction Fetch"]
        PC[("<span style="padding:4em 0;writing-mode:vertical-lr">Program Counter</span>")]
        ROM[("\n\nProgram\nMemory\n\n\n")]

        PC ==> ROM
    end

    STEP_IF ~~~ STEP_ID
    STEP_ID ~~~ STEP_EX
    STEP_EX ~~~ STEP_MEM
    STEP_MEM ~~~ STEP_WB

    WB_NODE(" ")

    WB ===> WB_NODE
    RF ==== WB_NODE
```

## Usagem

::: danger TO DO

Work in progress.

:::

## Diagrama RTL

![Diagrama de RTL do Top Level](/images/reference/components/top_level_netlist.svg){.w-full .dark-invert}

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_TOP_LEVEL.py" target="blank" style="float:right"><Badge type="tip" text="test_TOP_LEVEL.py &boxbox;" /></a>

<<< @/../test/test_TOP_LEVEL.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_top_level_case_1" />

Forma de onda:

![Forma de onda do caso de teste 1 do Top Level](/images/reference/components/tb_top_level_case_1.svg){.w-full .dark-invert}
