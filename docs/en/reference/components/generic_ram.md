---
outline: 2
---

# RAM <Badge type="info" text="GENERIC_RAM.vhd"/>

![RAM Logic Gate Diagram](../../public/images/referencia/componentes/generic_ram.drawio.svg)

[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_RAM.vhd).

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
- default: `10`

## Port Map

### `clock`

Clock input (signal that varies following the frequency of processor cycles).

- type: `std_logic`

### `enable`

Signal input that activates memory usage for read and/or write.

- type: `std_logic`

### `enable_read`

Signal input that activates memory read.

- type: `std_logic`

### `enable_write`

Signal input that activates memory write.

- type: `std_logic`

### `address`

Memory address input.

- type: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `source`

Data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `destination`

Data output with the value of memory at the address defined by `address`.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## RTL Diagram

![RAM RTL Diagram](../../public/images/referencia/componentes/generic_ram_netlist.svg)

## Test Cases

`test_GENERIC_RAM.py`.
[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_RAM.py).

::: danger TO DO

Work in progress.

:::
