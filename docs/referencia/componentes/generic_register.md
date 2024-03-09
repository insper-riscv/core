---
outline: 2
---

# Registrador

`GENERIC_REGISTER.vhd`

![Diagrama de portas do registrador](../../public/images/referencia/componentes/generic_register.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_REGISTER.vhd).

## Interface genérica

### `DATA_WIDTH`

Largura dos vetores de entrada e saída de dados.

- tipo: `natural`
- padrão: `XLEN`

## Interface de portas

### `clock`

Entrada do clock (sinal que varia seguindo a frequência de ciclos do
processador).

- tipo: `std_logic`

### `clear`

Entrada que reseta o contador.

- tipo: `std_logic`

### `enable`

::: danger TO DO

Escrever descrição enable

:::

- tipo: `std_logic`

### `source`

Entrada de dados.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`

### `destination`

Saída de dados com o valor armazenado no registrador.

- tipo: `std_logic_vector((DATA_WIDTH - 1) downto 0)`
- padrão: `0...0`

::: danger TO DO

Work in progress.

:::

## Diagrama RTL

::: danger TO DO

Diagrama a nível de registradores

:::

## Casos de teste

`test_GENERIC_REGISTER.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_REGISTER.py).

::: danger TO DO

Work in progress.

:::
