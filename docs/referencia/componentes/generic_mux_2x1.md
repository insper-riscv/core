---
outline: 2
---

# MUX 2x1

`GENERIC_MUX_2X1.vhd`

![Diagrama de portas do multiplexador 2 em 1](../../public/images/referencia/componentes/generic_mux_2x1.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_MUX_2X1.vhd).

## Interface genérica

### `DATA_WIDTH_0`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `DATA_WIDTH`

## Interface de portas

### `source_1`

Entrada de dados primária.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`

### `source_2`

Entrada de dados secundária.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`

### `selector`

Seletor que determina qual das entradas será usada.

- tipo: `std_logic`

### `destination`

Saída de dados com o valor de uma das entradas de dados (`source_1` ou `source_2`).

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`

## Diagrama RTL

::: danger TO DO

Diagrama a nível de registradores

:::

## Casos de teste

`test_GENERIC_MUX_2X1.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_MUX_2X1.py).

### Caso 1

Lógica combinacional:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `selector` &larr; `0`
- `destination` &rarr; `00001111000011110000111100001111`

### Caso 2

Lógica combinacional:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `selector` &larr; `1`
- `destination` &rarr; `11110000111100001111000011110000`

### Caso 3

Lógica combinacional:

- `source_1` &larr; `00000000000000000000000000000000`
- `source_2` &larr; `11111111111111111111111111111111`
- `selector` &larr; `0`
- `destination` &rarr; `00000000000000000000000000000000`

### Caso 4

Lógica combinacional:

- `source_1` &larr; `00000000000000000000000000000000`
- `source_2` &larr; `11111111111111111111111111111111`
- `selector` &larr; `1`
- `destination` &rarr; `11111111111111111111111111111111`
