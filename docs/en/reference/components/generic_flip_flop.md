---
outline: 2
---

# Flip Flop <Badge type="info" text="GENERIC_FLIP_FLOP.vhd"/>

![Diagrama de portas do flip flop](/images/referencia/componentes/generic_flip_flop.drawio.svg)

[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_FLIP_FLOP.vhd).

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

Entrada que reseta o flip flop.

- tipo: `std_logic`

### `enable`

::: danger TO DO

Escrever descrição enable

:::

- tipo: `std_logic`

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
- padrão: `0`

::: danger TO DO

Work in progress.

:::

## RTL Diagram

![Flip Flop RTL Diagram](/images/referencia/componentes/generic_flip_flop_netlist.svg)

## Test Cases

`test_GENERIC_FLIP_FLOP.py`.
[View source code](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_FLIP_FLOP.py).

### Case 1 <Badge type="info" text="Lógica sequencial" />

1.
   - `clear` &larr; `0`
   - `enable` &larr; `1`
   - `source` &larr; `1`
   - `state` &rarr; `0`
2.
   - `Clock` &larr; borda de subida
3.
   - `state` &rarr; `1`

### Case 2 <Badge type="info" text="Lógica sequencial" />

1.
   - `clear` &larr; `0`
   - `enable` &larr; `1`
   - `source` &larr; `0`
   - `state` &rarr; `0`
2.
   - `Clock` &larr; borda de subida
3.
   - `state` &rarr; `0`

### Case 3 <Badge type="info" text="Lógica sequencial" />

1.
   - `clear` &larr; `0`
   - `enable` &larr; `0`
   - `source` &larr; `1`
   - `state` &rarr; `0`
2.
   - `Clock` &larr; borda de subida
3.
   - `state` &rarr; `0`
