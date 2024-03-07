# Flip Flop

`GENERIC_FLIP_FLOP.vhd`

![Diagrama de portas do flip flop](../../public/images/referencia/componentes/generic_flip_flop.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_FLIP_FLOP.vhd).

## Interface genérica


::: danger TO DO

Work in progress.

:::

## Interface de portas

### `clock`

Entrada do clock (sinal que varia seguindo a frequência de ciclos do processador).

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

## Diagrama RTL

::: danger TO DO

Diagrama a nível de registradores

:::

## Casos de teste

`test_GENERIC_FLIP_FLOP.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_FLIP_FLOP.py).

### Caso 1

Lógica combinacional:

- `clear` &larr; `0`
- `enable` &larr; `1`
- `source` &larr; `1`
- `state` &rarr; `1`

### Caso 2

Lógica combinacional:

- `clear` &larr; `0`
- `enable` &larr; `1`
- `source` &larr; `0`
- `state` &rarr; `0`

### Caso 3

Lógica combinacional:

- `clear` &larr; `1`
- `enable` &larr; `0`
- `source` &larr; `1`
- `state` &rarr; `0`

::: warning TO DO

Review.

:::