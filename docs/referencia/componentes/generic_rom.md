---
outline: 2
---

# ROM <Badge type="info" text="GENERIC_ROM.vhd"/>

![Diagrama de portas da memória ROM](/images/referencia/componentes/generic_rom.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_ROM.vhd).

## Interface genérica

### `DATA_WIDTH`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `XLEN`

### `ADDRESS_WIDTH`

Largura do vetor de entrada de endereço de memória.

- tipo: `natural`
- padrão: `XLEN`

### `ADDRESSABLE_WIDTH`

Expoente da potência que determina o tamanho da memória.

- tipo: `natural`
- padrão: `7`

## Interface de portas

### `address`

Entrada de endereço da memória.

- tipo: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `destination`

Saída de dados com o valor da memória no endereço definido por `address`.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## Diagrama RTL

<img src="/images/referencia/componentes/generic_rom_netlist.svg" alt="Diagrama de RTL da ROM" style="width: 100%; background-color: white;">

## Casos de teste

`test_GENERIC_ROM.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ROM.py).

::: danger TO DO

Work in progress.

:::
