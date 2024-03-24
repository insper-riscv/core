---
outline: 2
---

# Debounce <Badge type="info" text="GENERIC_DEBOUNCE.vhd"/>

::: danger TO DO

Diagrama de portas

:::

[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_DEBOUNCE.vhd).

## Generic Map

::: danger TO DO

Work in progress.

:::

## Port Map

### `clock`

Entrada do clock (sinal que varia seguindo a frequência de ciclos do
processador).

- tipo: `std_logic`

### `clear`

Entrada que reseta o debounce.

- tipo: `std_logic`
- padrão: `0`

### `source`

::: danger TO DO

Escrever descrição source

:::

- tipo: `std_logic`

### `state`

::: danger TO DO

Escrever descrição state

:::

- tipo: `std_logic`

::: danger TO DO

Work in progress.

:::

## RTL Diagram

![Debounce RTL Diagram](../../public/images/referencia/componentes/generic_debounce_netlist.svg)

## Test Cases

`test_GENERIC_DEBOUNCE.py`.
[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_DEBOUNCE.py).

::: danger TO DO

Work in progress.

:::
