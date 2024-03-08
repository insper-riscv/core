# Banco de Registradores

`GENERIC_REGISTERS_BANK.vhd`

![Diagrama de portas do banco de registradores](../../public/images/referencia/componentes/generic_registers_bank.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_REGISTERS_BANK.vhd).

## Interface genérica

### `DATA_WIDTH_0`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `DATA_WIDTH`

### `ADDRESS_WIDTH`

Largura dos vetores de entrada e saída de endereços.

- tipo: `natural`
- padrão: `32`

## Interface de portas

### `clock`

Entrada do clock (sinal que varia seguindo a frequência de ciclos do processador).

- tipo: `std_logic`

### `enable`

Entrada de sinal que ativa uso do banco de registradores para armazenar valor.

- tipo: `std_logic`

### `address_destination`

Entrada de endereço de registrador para armazenar valor.

- tipo: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `address_source_1`

Entrada de endereço de registrador primária.

- tipo: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `address_source_2`

Entrada de endereço de registrador secundária.

- tipo: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `data_destination`

Entrada de valor para armazenar em registrador.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`

### `data_source_1`

Saída de valor de registrador primária.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`

### `data_source_2`

Saída de valor de registrador secundária.

- tipo: `std_logic_vector((DATA_WIDTH_0 - 1) downto 0)`

## Diagrama RTL

::: danger TO DO

Diagrama a nível de registradores

:::

## Casos de teste

`test_GENERIC_REGISTERS_BANK.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_REGISTERS_BANK.py).

::: danger TO DO

Work in progress.

:::
