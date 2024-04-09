---
outline: 2
---

# Arquivo de registradores

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/RV32I_REGISTER_FILE.vhd" target="blank" style="float:right"><Badge type="tip" text="RV32I_REGISTER_FILE.vhd &boxbox;" /></a>

<<< @/../src/RV32I_REGISTER_FILE.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container>

<!--@include: @/.includes/rv32i_register_file-topology.md-->

</pan-container>

## Interface genérica

### `DATA_WIDTH`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `XLEN`

### `ADDRESS_WIDTH`

Largura dos vetores de entrada e saída de endereços.

- tipo: `natural`
- padrão: `32`

## Interface de portas

### `clock` <Badge type="success" text="INPUT" />

Entrada do sinal de clock.

- Tipo: `std_logic`

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

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `data_source_1`

Saída de valor de registrador primária.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `data_source_2`

Saída de valor de registrador secundária.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

## Diagrama RTL

<pan-container>

![Diagrama de RTL do arquivo de registradores](/images/reference/components/rv32i_register_file_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_RV32I_REGISTER_FILE.py" target="blank" style="float:right"><Badge type="tip" text="test_RV32I_REGISTER_FILE.py &boxbox;" /></a>

<<< @/../test/test_RV32I_REGISTER_FILE.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_rv32i_register_file_case_1" />

Forma de onda:

<pan-container :grid="false">

<img src="/images/reference/components/tb_rv32i_register_file_case_1.svg" alt="Caso de teste 1 do Arquivo de Registradores" style="width: 100%; background-color: white;">

</pan-container>
