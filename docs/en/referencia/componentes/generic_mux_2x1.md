---
outline: 2
---

# MUX 2:1 <Badge type="info" text="GENERIC_MUX_2X1.vhd"/>

![MUX 2:1 Logic Gate Diagram](../../public/images/referencia/componentes/generic_mux_2x1.drawio.svg)

[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_MUX_2X1.vhd).

## Generic Map

### `DATA_WIDTH`

Width of input and output data vectors.

- type: `natural`
- default: `XLEN`

## Port Map

### `source_1`

Primary data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `source_2`

Secondary data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `selector`

Selector that determines which input of data will be used.

- type: `std_logic`

### `destination`

Output data with the value of one of the data inputs (`source_1` or `source_2`).

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## RTL Diagram

![MUX 2:1 RTL Diagram](../../public/images/referencia/componentes/generic_mux_2x1_netlist.svg)

## Test Cases

`test_GENERIC_MUX_2X1.py`.
[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_MUX_2X1.py).

### Case 1

Combinational Logic:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `selector` &larr; `0`
- `destination` &rarr; `00001111000011110000111100001111`

### Case 2

Combinational Logic:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `selector` &larr; `1`
- `destination` &rarr; `11110000111100001111000011110000`

### Case 3

Combinational Logic:

- `source_1` &larr; `00000000000000000000000000000000`
- `source_2` &larr; `11111111111111111111111111111111`
- `selector` &larr; `0`
- `destination` &rarr; `00000000000000000000000000000000`

### Case 4

Combinational Logic:

- `source_1` &larr; `00000000000000000000000000000000`
- `source_2` &larr; `11111111111111111111111111111111`
- `selector` &larr; `1`
- `destination` &rarr; `11111111111111111111111111111111`
