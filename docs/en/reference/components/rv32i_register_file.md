---
outline: 2
---

# Arquivo de registradores

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/RV32I_REGISTER_FILE.vhd" target="blank" style="float:right"><Badge type="tip" text="RV32I_REGISTER_FILE.vhd &boxbox;" /></a>

<<< @/../src/TOP_LEVEL.vhd{vhdl:line-numbers}

:::

## Topology

![Topologia do banco de registradores](/images/reference/components/rv32i_register_file.drawio.svg)

## Generic interface

### `DATA_WIDTH`

Largura dos vetores de entrada e saída de dados.

- Type: `natural`
- Default: `XLEN`

### `ADDRESS_WIDTH`

Largura dos vetores de entrada e saída de endereços.

- Type: `natural`
- Default: `32`

## Port interface

### `clock` <Badge type="warning" text="INPUT" />

Entrada do sinal de clock.

- Type: `std_logic`

### `enable`

Entrada de sinal que ativa uso do banco de registradores para armazenar valor.

- Type: `std_logic`

### `address_destination`

Entrada de endereço de registrador para armazenar valor.

- Type: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `address_source_1`

Entrada de endereço de registrador primária.

- Type: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `address_source_2`

Entrada de endereço de registrador secundária.

- Type: `std_logic_vector((ADDRESS_WIDTH - 1) downto 0)`

### `data_destination`

Entrada de valor para armazenar em registrador.

- Type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `data_source_1`

Saída de valor de registrador primária.

- Type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `data_source_2`

Saída de valor de registrador secundária.

- Type: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## RTL View

<img src="/images/reference/components/rv32i_register_file_netlist.svg" alt="RTL view from arquivo de registradores" style="width: 100%; background-color: white;">

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_RV32I_REGISTER_FILE.py" target="blank" style="float:right"><Badge type="tip" text="test_RV32I_REGISTER_FILE.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

### Case 1 <Badge type="info" text="tb_RV32I_REGISTER_FILE_case_1" />

Waveform:

<img src="/images/reference/components/tb_RV32I_REGISTER_FILE_case_1.svg" alt="Caso de teste 1 do Arquivo de Registradores" style="width: 100%; background-color: white;">
