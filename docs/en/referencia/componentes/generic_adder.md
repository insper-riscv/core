---
outline: 2
---

# Adder <Badge type="info" text="GENERIC_ADDER.vhd"/>

![Adder Logic Gate Diagram](../../public/images/referencia/componentes/generic_adder.drawio.svg)

[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_ADDER.vhd).

## Generic Map

### `DATA_WIDTH`

Width of input and output data vectors.

- type: `natural`
- default: `XLEN`

### `DEFAULT_SOURCE_2`

Default value of increment. Eliminates the need for `source_2`.

- type: `integer`
- default: `1`

## Port Map

### `source_1`

Primary data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `source_2`

Secondary data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- default: `to_signed(DEFAULT_SOURCE_1, DATA_WIDTH)`

### `destination`

Output data with the result of `source_1 + source_2`.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## RTL Diagram

![Adder RTL Diagram](../../public/images/referencia/componentes/generic_adder_netlist.svg)

## Test Cases

`test_GENERIC_ADDER.py`.
[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ADDER.py).

### Case 1 <Badge type="info" text="Combinational Logic" />

- `source_1` &larr; `00000000000000000000000000000000`
- `source_2` &larr; `00000000000000000000000000000000`
- `destination` &rarr; `00000000000000000000000000000000`

### Case 2 <Badge type="info" text="Combinational Logic" />

- `source_1` &larr; `10101010101010101010101010101010`
- `source_2` &larr; `01010101010101010101010101010101`
- `destination` &rarr; `11111111111111111111111111111111`

### Case 3 <Badge type="info" text="Combinational Logic" />

- `source_1` &larr; `00101010101010101010101010101010`
- `source_2` &larr; `00101010101010101010101010101010`
- `destination` &rarr; `01010101010101010101010101010100`

### Case 4 <Badge type="info" text="Combinational Logic" />

- `source_1` &larr; `11111111111111111111111111111110`
- `source_2` &larr; `00000000000000000000000000000001`
- `destination` &rarr; `11111111111111111111111111111111`

