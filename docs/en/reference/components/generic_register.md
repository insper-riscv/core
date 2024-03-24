---
outline: 2
---

# Register <Badge type="info" text="GENERIC_REGISTER.vhd"/>

![Register Logic Gate Diagram](/images/referencia/componentes/generic_register.drawio.svg)

[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_REGISTER.vhd).

## Generic Map

### `DATA_WIDTH`

Width of input and output data vectors.

- type: `natural`
- default: `XLEN`

## Port Map

### `clock`

Clock input (signal that varies following the frequency of processor cycles).

- type: `std_logic`

### `clear`

Input that resets the counter.

- type: `std_logic`

### `enable`

Signal input that stores the value of data input into the register.

- type: `std_logic`

### `source`

Data input.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `destination`

Data output with the value stored in the register.

- type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- default: `0...0`

## RTL Diagram

![Register RTL Diagram](/images/referencia/componentes/generic_register_netlist.svg)

## Test Cases

`test_GENERIC_REGISTER.py`.
[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_REGISTER.py).

::: danger TO DO

Work in progress.

:::
