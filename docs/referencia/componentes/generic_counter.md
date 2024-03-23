---
outline: 2
---

# Contador <Badge type="info" text="GENERIC_COUNTER.vhd"/>

![Diagrama de portas do contador](../../public/images/referencia/componentes/generic_counter.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_COUNTER.vhd).

## Interface genérica

### `DEFAULT_OVERFLOW`

Valor padrão de overflow.

- tipo: `natural`
- padrão: `CLOCK_FREQUENCY`

## Interface de portas

### `clock`

Entrada do clock (sinal que varia seguindo a frequência de ciclos do processador).

- tipo: `std_logic`

### `clear`

Entrada que reseta o contador.

- tipo: `std_logic`

### `update`

Entrada que atualiza o valor de overflow.

- tipo: `std_logic`

### `source`

::: danger TO DO

Escrever descrição source

:::

- tipo: `std_logic_vector(4 downto 0)`

### `state`

::: danger TO DO

Escrever descrição state

:::

- tipo: `std_logic`
- padrão: `0`

::: danger TO DO

Work in progress.

:::

## Diagrama RTL

<img src="../../public/images/referencia/componentes/generic_counter_netlist.svg" alt="Diagrama de RTL do contador" style="width: 100%; background-color: white;">

## Casos de teste

`test_GENERIC_COUNTER.py`.
[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_COUNTER.py).

::: danger TO DO

Work in progress.

:::
