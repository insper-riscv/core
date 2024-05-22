---
outline: 2
---

# Registrador

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_REGISTER.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_REGISTER.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_REGISTER.vhd{vhdl:line-numbers}

:::

## Topology

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_REGISTER"]
        direction LR
        subgraph GENERIC ["generic map"]
            direction LR
            DATA_WIDTH
        end
        F[("destination")]
        style F scale:1.3
    end
    A(((clock))) ---> TOP
    B([clear]) ---> TOP
    C([enable]) ---> TOP
    D([source]) -- DATA_WIDTH ---> TOP
    TOP -- DATA_WIDTH ---> E([destination])
```

## Generic interface

### `DATA_WIDTH` <Badge type="neutral" text="GENERIC" />

Largura dos vetores de dados `source` e `destination`.

- Type: `natural`
- Default: `XLEN` (external constant)

## Port interface

### `clock` <Badge type="success" text="INPUT" />

Entrada do sinal de clock.

- Type: `std_logic`

### `clear` <Badge type="success" text="INPUT" />

::: danger TO DO

Descrição.

:::

- Type: `std_logic`

### `enable` <Badge type="success" text="INPUT" />

::: danger TO DO

Descrição.

:::

- Type: `std_logic`

### `source` <Badge type="success" text="INPUT" />

::: danger TO DO

Descrição.

:::

- Type: `std_logic_vector`
- Width: variable`(DATA_WIDTH - 1) downto 0`

### `destination` <Badge type="danger" text="OUTPUT" />

::: danger TO DO

Descrição.

:::

- Type: `std_logic_vector`
- Width: variable`(DATA_WIDTH - 1) downto 0`
- Default: `"0...0"`

## Usage

```vhdl
REGISTER_1 : entity WORK.GENERIC_REGISTER
    generic map (
        DATA_WIDTH => 32
    )
    port map (
        clock       => clock,
        clear       => signal_clear,
        enable      => signal_enable,
        source      => signal_source,
        destination => signal_destination
    );
```

## RTL View

![RTL view from Registrador](/images/reference/components/generic_register_netlist.svg){.w-full .dark-invert}

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_REGISTER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_REGISTER.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

### Case 1 <Badge type="info" text="tb_generic_register_case_1" />

Waveform:

![Waveform from caso de teste 1 do Registrador](/images/reference/components/tb_generic_register_case_1.svg){.w-full .dark-invert}
