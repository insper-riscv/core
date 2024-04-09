---
outline: 2
---

# Extensor de Sinal

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_SIGNAL_EXTENDER.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_SIGNAL_EXTENDER.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_SIGNAL_EXTENDER.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

<!--@include: @/.includes/generic_signal_extender-topology.md-->

</pan-container>

## Interface genérica

### `SOURCE_WIDTH` <Badge type="neutral" text="GENERIC" />
- Tipo: `natural`
- Padrão: `XLEN` (constante externa)

### `DESTINATION_WIDTH` <Badge type="neutral" text="GENERIC" />
- Tipo: `natural`
- Padrão: `XLEN` (constante externa)

## Interface de portas

### `source` <Badge type="success" text="INPUT" />

Vetor de entrada de dados.

- Tipo: `std_logic_vector`
- Largura: `(SOURCE_WIDTH - 1) downto 0`

### `enable_unsigned` <Badge type="success" text="INPUT" />

::: danger TO DO

Descrição.

:::

- Tipo: `std_logic`

### `destination` <Badge type="danger" text="OUTPUT" />

Vetor de entrada de dados com sinal estendido.

- Tipo: `std_logic_vector`
- Largura: `(DESTINATION_WIDTH - 1) downto 0`


## Diagrama RTL

<pan-container>

![Diagrama de RTL do Extensor de Sinal](/images/reference/components/generic_signal_extender_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_SIGNAL_EXTENDER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_SIGNAL_EXTENDER.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_SIGNAL_EXTENDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Caso 1 <Badge type="info" text="tb_generic_signal_extender_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do Extensor de Sinal](/images/reference/components/tb_generic_signal_extender_case_1.svg){.w-full .dark-invert}

</pan-container>

```

:::
