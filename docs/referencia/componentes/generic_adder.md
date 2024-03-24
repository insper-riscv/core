---
outline: 2
---

# Somador <Badge type="info" text="GENERIC_ADDER.vhd"/>

![Diagrama de portas do somador](/images/referencia/componentes/generic_adder.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_ADDER.vhd).

## Interface genérica

### `DATA_WIDTH`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `XLEN`

### `DEFAULT_SOURCE_2`

Valor padrão de incremento. Dispensa necessidade de `source_2`.

- tipo: `integer`
- padrão: `1`

## Interface de portas

### `source_1`

Entrada de dados primária.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `source_2`

Entrada de dados secundária.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- padrão: `to_signed(DEFAULT_SOURCE_1, DATA_WIDTH)`

### `destination`

Saída de dados com o resultado de `source_1 + source_2`.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## Diagrama RTL

![Diagrama RTL do somador](/images/referencia/componentes/generic_adder_netlist.svg)
<!-- <img src="/images/referencia/componentes/generic_adder_netlist.svg" alt="Diagrama de RTL do somador" style="width: 100%; background-color: white;"> -->

## Casos de teste

`test_GENERIC_ADDER.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ADDER.py).

### Caso 1 <Badge type="info" text="Lógica combinacional" />

- `source_1` &larr; `00000000000000000000000000000000`
- `source_2` &larr; `00000000000000000000000000000000`
- `destination` &rarr; `00000000000000000000000000000000`

### Caso 2 <Badge type="info" text="Lógica combinacional" />

- `source_1` &larr; `10101010101010101010101010101010`
- `source_2` &larr; `01010101010101010101010101010101`
- `destination` &rarr; `11111111111111111111111111111111`

### Caso 3 <Badge type="info" text="Lógica combinacional" />

- `source_1` &larr; `00101010101010101010101010101010`
- `source_2` &larr; `00101010101010101010101010101010`
- `destination` &rarr; `01010101010101010101010101010100`

### Caso 4 <Badge type="info" text="Lógica combinacional" />

- `source_1` &larr; `11111111111111111111111111111110`
- `source_2` &larr; `00000000000000000000000000000001`
- `destination` &rarr; `11111111111111111111111111111111`
