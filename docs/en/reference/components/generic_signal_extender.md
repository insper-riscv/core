---
outline: 2
---

# Extensor de Sinal

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_SIGNAL_EXTENDER.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_SIGNAL_EXTENDER.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_SIGNAL_EXTENDER.vhd{vhdl:line-numbers}

:::

## Topology

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_SIGNAL_EXTENDER"]
        direction LR
        subgraph GENERIC ["generic map"]
            direction LR
            SOURCE_WIDTH
            DESTINATION_WIDTH
        end
    end
    E([enable_unsigned]) ---> TOP
    F([source]) -- SOURCE_WIDTH ---> TOP
    TOP -- DESTINATION_WIDTH ---> G([destination])
```

## Generic interface

### `SOURCE_WIDTH` <Badge type="tip" text="GENERIC" />
- Type: `natural`
- Default: `XLEN` (external constant)

### `DESTINATION_WIDTH` <Badge type="tip" text="GENERIC" />
- Type: `natural`
- Default: `XLEN` (external constant)

## Port interface

### `source` <Badge type="warning" text="INPUT" />

Vetor de entrada de dados.

- Type: `std_logic_vector`
- Width: variable`(SOURCE_WIDTH - 1) downto 0`

### `enable_unsigned` <Badge type="warning" text="INPUT" />

::: danger TO DO

Descrição.

:::

- Type: `std_logic`

### `destination` <Badge type="danger" text="OUTPUT" />

Vetor de entrada de dados com sinal estendido.

- Type: `std_logic_vector`
- Width: variable`(DESTINATION_WIDTH - 1) downto 0`


## RTL View

![RTL view from Extensor de Sinal](/images/reference/components/generic_signal_extender_netlist.svg){.w-full .dark-invert}

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_SIGNAL_EXTENDER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_SIGNAL_EXTENDER.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Case 1 <Badge type="info" text="tb_generic_signal_extender_case_1" />

Waveform:

![Waveform from caso de teste 1 do Extensor de Sinal](/images/reference/components/tb_generic_signal_extender_case_1.svg){.w-full .dark-invert}
```

:::
