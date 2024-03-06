# MUX 4x1

`GENERIC_MUX_4X1.vhd`

![Diagrama de portas do multiplexador 4 em 1](../../public/images/referencia/componentes/generic_mux_4x1.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_MUX_4X1.vhd).

## Interface genérica

### `DATA_WIDTH_0`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `DATA_WIDTH`

## Interface de portas

### `source_1`

Entrada de dados primária.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`
- padrão: `00000000000000000000000000000000`

### `source_2`

Entrada de dados secundária.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`
- padrão: `00000000000000000000000000000000`

### `source_3`

Entrada de dados terciária.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`
- padrão: `00000000000000000000000000000000`

### `source_4`

Entrada de dados quaternária.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`
- padrão: `00000000000000000000000000000000`

### `selector`

Seletor que determina qual das entradas será usada.

- tipo: `std_logic_vector(1 downto 0)`

### `destination`

Saída de dados com o valor de uma das entradas de dados (`source_1`, `source_2`, `source_3` ou `source_4`).

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`

## Diagrama RTL

::: danger TO DO

Diagrama a nível de registradores

:::

## Casos de teste

`test_GENERIC_MUX_4X1.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_MUX_4X1.py).

::: danger TO DO

Work in progress.

:::
