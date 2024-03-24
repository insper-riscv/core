---
outline: 2
---

# Flip Flop <Badge type="info" text="GENERIC_FLIP_FLOP.vhd"/>

![Diagrama de portas do flip flop](/images/referencia/componentes/generic_flip_flop.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_FLIP_FLOP.vhd).

## Interface genérica

::: danger TO DO

Work in progress.

:::

## Interface de portas

### `clock`

Entrada do clock (sinal que varia seguindo a frequência de ciclos do
processador).

- tipo: `std_logic`

### `clear`

Entrada que reseta o flip flop.

- tipo: `std_logic`

### `enable`

::: danger TO DO

Escrever descrição enable

:::

- tipo: `std_logic`

### `source`

::: danger TO DO

Escrever descrição source

:::

- tipo: `std_logic`

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

<img src="/images/referencia/componentes/generic_flip_flop_netlist.svg" alt="Diagrama de RTL do flip flop" style="width: 100%; background-color: white;">

## Casos de teste <Badge type="info" text="test_GENERIC_FLIP_FLOP.py" />

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_FLIP_FLOP.py).

### Caso 1 <Badge type="info" text="tb_GENERIC_FLIP_FLOP_case_1" />

Lógica sequencial:

<img src="/images/referencia/componentes/tb_GENERIC_FLIP_FLOP_case_1.svg" alt="Caso de teste 1 do Flip Flop" style="width: 100%; background-color: white;">
