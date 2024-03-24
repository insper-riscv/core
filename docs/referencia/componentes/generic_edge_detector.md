---
outline: 2
---

# Detector de Borda <Badge type="info" text="GENERIC_EDGE_DETECTOR.vhd"/>

![Diagrama de portas do detector de borda](/images/referencia/componentes/generic_edge_detector.drawio.svg)

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_EDGE_DETECTOR.vhd).

## Interface genérica

::: danger TO DO

Work in progress.

:::

## Interface de portas

### `clock`

Entrada do clock (sinal que varia seguindo a frequência de ciclos do processador).

- tipo: `std_logic`

### `source`

::: danger TO DO

Escrever descrição source

:::

- tipo: `std_logic`

### `pulse`

::: danger TO DO

Escrever descrição pulse

:::

- tipo: `std_logic`

::: danger TO DO

Work in progress.

:::

## Diagrama RTL

<img src="/images/referencia/componentes/generic_edge_detector_netlist.svg" alt="Diagrama de RTL do detector de borda" style="width: 100%; background-color: white;">

## Casos de teste <Badge type="info" text="test_GENERIC_EDGE_DETECTOR.py" />

[Ver código fonte](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_EDGE_DETECTOR.py).

### Caso 1 <Badge type="info" text="tb_GENERIC_EDGE_DETECTOR_case_1" />

Lógica sequencial:

<img src="/images/referencia/componentes/tb_GENERIC_EDGE_DETECTOR_case_1.svg" alt="Caso de teste 1 do Detector de Borda" style="width: 100%; background-color: white;">

### Caso 2 <Badge type="info" text="tb_GENERIC_EDGE_DETECTOR_case_2" />

Lógica sequencial:

<img src="/images/referencia/componentes/tb_GENERIC_EDGE_DETECTOR_case_2.svg" alt="Caso de teste 2 do Detector de Borda" style="width: 100%; background-color: white;">
