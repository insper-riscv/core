---
outline: 2
---

# RAM <Badge type="info" text="GENERIC_RAM.vhd"/>

![Diagrama de portas da memória RAM](../../public/images/referencia/componentes/generic_ram.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_RAM.vhd).

## Interface genérica

### `DATA_WIDTH`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `XLEN`

### `ADDRESS_WIDTH`

Largura do vetor de entrada de endereço de memória.

- tipo: `natural`
- padrão: `32`

### `ADDRESSABLE_WIDTH`

::: danger TO DO

Escrever descrição de ADDRESSABLE_WIDTH

:::

- tipo: `natural`
- padrão: `8`

## Interface de portas

### `clock`

Entrada do clock (sinal que varia seguindo a frequência de ciclos do
processador).

- tipo: `std_logic`

### `enable`

Entrada de sinal que ativa uso da memória para leitura e/ou escrita.

- tipo: `std_logic`

### `enable_read`

Entrada de sinal que ativa leitura da memória.

- tipo: `std_logic`

### `enable_write`

Entrada de sinal que ativa escrita da memória.

- tipo: `std_logic`

### `address`

Entrada de endereço da memória.

- tipo: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `source`

Entrada de dados.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `destination`

Saída de dados com o valor da memória no endereço definido por `address`.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## Diagrama RTL

<img src="../../public/images/referencia/componentes/generic_ram_netlist.svg" alt="Diagrama de RTL da RAM" style="width: 100%; background-color: white;">

## Casos de teste

`test_GENERIC_RAM.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_RAM.py).

::: danger TO DO

Work in progress.

:::
