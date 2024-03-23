---
outline: 2
---

# MUX 4:1 <Badge type="info" text="GENERIC_MUX_4X1.vhd"/>

![MUX 4:1 Logic Gate Diagram](../../public/images/referencia/componentes/generic_mux_4x1.drawio.svg)

[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_MUX_4X1.vhd).

## Generic Map

### `DATA_WIDTH`

Width of input and output data vectors.

- type: `natural`
- default: `XLEN`

## Port Map

### `source_1`

Primary data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- default: `0...0`

### `source_2`

Secondary data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- default: `0...0`

### `source_3`

Tertiary data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- default: `0...0`

### `source_4`

Quaternary data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- default: `0...0`

### `selector`

Selector that determines which input of data will be used.

- type: `std_logic_vector(1 downto 0)`

### `destination`

Output data with the value of one of the data inputs (`source_1`, `source_2`, `source_3`, or `source_4`).

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## RTL Diagram

![MUX 4:1 RTL Diagram](../../public/images/referencia/componentes/generic_mux_4x1_netlist.svg)

## Test Cases

`test_GENERIC_MUX_4X1.py`.
[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_MUX_4X1.py).

### Case 1

Combinational Logic:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `source_3` &larr; `00000000111111111111111100000000`
- `source_4` &larr; `11111111000000000000000011111111`
- `selector` &larr; `00`
- `destination` &rarr; `00001111000011110000111100001111`

### Case 2

Combinational Logic:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `source_3` &larr; `00000000111111111111111100000000`
- `source_4` &larr; `11111111000000000000000011111111`
- `selector` &larr; `01`
- `destination` &rarr; `11110000111100001111000011110000`

### Case 3

Combinational Logic:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `source_3` &larr; `00000000111111111111111100000000`
- `source_4` &larr; `11111111000000000000000011111111`
- `selector` &larr; `10`
- `destination` &rarr; `00000000111111111111111100000000`

### Case 4

Combinational Logic:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `source_3` &larr; `00000000111111111111111100000000`
- `source_4` &larr; `11111111000000000000000011111111`
- `selector` &larr; `11`
- `destination` &rarr; `11111111000000000000000011111111`

