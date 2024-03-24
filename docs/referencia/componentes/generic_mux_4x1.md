---
outline: 2
---

# MUX 4x1 <Badge type="info" text="GENERIC_MUX_4X1.vhd"/>

![Diagrama de portas do multiplexador 4 em 1](/images/referencia/componentes/generic_mux_4x1.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_MUX_4X1.vhd).

## Interface genérica

### `DATA_WIDTH`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `XLEN`

## Interface de portas

### `source_1`

Entrada de dados primária.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- padrão: `0...0`

### `source_2`

Entrada de dados secundária.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- padrão: `0...0`

### `source_3`

Entrada de dados terciária.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- padrão: `0...0`

### `source_4`

Entrada de dados quaternária.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- padrão: `0...0`

### `selector`

Seletor que determina qual das entradas será usada.

- tipo: `std_logic_vector(1 downto 0)`

### `destination`

Saída de dados com o valor de uma das entradas de dados (`source_1`, `source_2`,
`source_3` ou `source_4`).

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## Diagrama RTL

<img src="/images/referencia/componentes/generic_mux_4x1_netlist.svg" alt="Diagrama de RTL do mux 4x1" style="width: 100%; background-color: white;">

## Casos de teste

`test_GENERIC_MUX_4X1.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_MUX_4X1.py).

### Caso 1

Lógica combinacional:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `source_3` &larr; `00000000111111111111111100000000`
- `source_4` &larr; `11111111000000000000000011111111`
- `selector` &larr; `00`
- `destination` &rarr; `00001111000011110000111100001111`

### Caso 2

Lógica combinacional:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `source_3` &larr; `00000000111111111111111100000000`
- `source_4` &larr; `11111111000000000000000011111111`
- `selector` &larr; `01`
- `destination` &rarr; `11110000111100001111000011110000`

### Caso 3

Lógica combinacional:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `source_3` &larr; `00000000111111111111111100000000`
- `source_4` &larr; `11111111000000000000000011111111`
- `selector` &larr; `10`
- `destination` &rarr; `00000000111111111111111100000000`

### Caso 4

Lógica combinacional:

- `source_1` &larr; `00001111000011110000111100001111`
- `source_2` &larr; `11110000111100001111000011110000`
- `source_3` &larr; `00000000111111111111111100000000`
- `source_4` &larr; `11111111000000000000000011111111`
- `selector` &larr; `11`
- `destination` &rarr; `11111111000000000000000011111111`
