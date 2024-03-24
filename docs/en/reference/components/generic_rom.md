---
outline: 2
---

# ROM <Badge type="info" text="GENERIC_ROM.vhd"/>

![ROM Logic Gate Diagram](/images/referencia/componentes/generic_rom.drawio.svg)

[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_ROM.vhd).

## Generic Map

### `DATA_WIDTH`

Width of input and output data vectors.

- type: `natural`
- default: `XLEN`

### `ADDRESS_WIDTH`

Width of memory address input vector.

- type: `natural`
- default: `XLEN`

### `ADDRESSABLE_WIDTH`

Exponent of the power that determines memory size.

- type: `natural`
- default: `7`

## Port Map

### `address`

Memory address input.

- type: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `destination`

Data output with the value of memory at the address defined by `address`.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## RTL Diagram

![ROM RTL Diagram](/images/referencia/componentes/generic_rom_netlist.svg)

## Test Cases

`test_GENERIC_ROM.py`.
[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ROM.py).

::: danger TO DO

Work in progress.

:::
