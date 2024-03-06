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

::: danger TO DO

Work in progress.

:::
