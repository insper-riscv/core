---
outline: 2
---

# Multiplexador 4x1

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_MUX_4X1.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_MUX_4X1.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_MUX_4X1.vhd{vhdl:line-numbers}

:::

## Topology

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_MUX_4X1"]
        direction LR
        subgraph GENERIC ["generic map"]
            direction LR
            DATA_WIDTH
        end
        E("GENERIC_MUX_2X1")
        click E href "./generic_mux_2x1.html"
    end
    A([source_1]) -- DATA_WIDTH ---> TOP
    B([source_2]) -- DATA_WIDTH ---> TOP
    C([selector]) ---> TOP
    TOP -- DATA_WIDTH ---> D([destination])
```

## Generic interface

### `DATA_WIDTH` <Badge type="tip" text="GENERIC" />

Largura dos vetores de entrada e saída de dados.

- Type: `natural`
- Default: `XLEN` (external constant)

## Port interface

### `source_1` <Badge type="warning" text="INPUT" />

Vetor de entrada primário. `destination <= source_1` se `selector = "00"`.

- Type: `std_logic_vector`
- Width: variable`(DATA_WIDTH - 1) downto 0`

### `source_2` <Badge type="warning" text="INPUT" />

Vetor de entrada secundário. `destination <= source_2` se `selector = "01"`.

- Type: `std_logic_vector`
- Width: variable`(DATA_WIDTH - 1) downto 0`

### `source_3` <Badge type="warning" text="INPUT" />

Vetor de entrada terciário. `destination <= source_3` se `selector = "10"`.

- Type: `std_logic_vector`
- Width: variable`(DATA_WIDTH - 1) downto 0`

### `source_4` <Badge type="warning" text="INPUT" />

Vetor de entrada quaternário. `destination <= source_4` se `selector = "11"`.

- Type: `std_logic_vector`
- Width: variable`(DATA_WIDTH - 1) downto 0`

### `selector` <Badge type="warning" text="INPUT" />

Seleção do vetor de saída de `destination`.

- Type: `std_logic`

### `destination` <Badge type="danger" text="OUTPUT" />

Vetor de saída.

- Type: `std_logic_vector`
- Width: variable`(DATA_WIDTH - 1) downto 0`

## Usage

```vhdl
MUX_1 : entity WORK.GENERIC_MUX_4X1
    generic map (
        DATA_WIDTH_0 => 32
    )
    port map (
        source_1    => signal_source_1,
        source_2    => signal_source_2,
        source_3    => signal_source_3,
        source_4    => signal_source_4,
        selector    => signal_selector,
        destination => signal_destination
    );
```

## RTL View

![RTL view from mux 4x1](/images/reference/components/generic_mux_4x1_netlist.svg){.w-full .dark-invert}

### Dependências

- `MUX_1`: [Multiplexador 2x1](./generic_mux_2x1.html)
- `MUX_2`: [Multiplexador 2x1](./generic_mux_2x1.html)

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_MUX_4X1.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_MUX_4X1.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

### Case 1 <Badge type="info" text="tb_generic_mux_4x1_case_1" />

Waveform:

![Waveform from caso de teste 1 do Flip Flop](/images/reference/components/tb_generic_mux_4x1_case_1.svg){.w-full .dark-invert}
