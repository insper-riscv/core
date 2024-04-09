---
outline: 2
---

# Registrador

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_REGISTER.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_REGISTER.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_REGISTER.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

<!--@include: @/.includes/generic_register-topology.md-->

</pan-container>

## Interface genérica

### `DATA_WIDTH` <Badge type="neutral" text="GENERIC" />

Largura dos vetores de dados `source` e `destination`.

- Tipo: `natural`
- Padrão: `XLEN` (constante externa)

## Interface de portas

### `clock` <Badge type="success" text="INPUT" />

Entrada do sinal de clock.

- Tipo: `std_logic`

### `clear` <Badge type="success" text="INPUT" />

::: danger TO DO

Descrição.

:::

- Tipo: `std_logic`

### `enable` <Badge type="success" text="INPUT" />

::: danger TO DO

Descrição.

:::

- Tipo: `std_logic`

### `source` <Badge type="success" text="INPUT" />

::: danger TO DO

Descrição.

:::

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`

### `destination` <Badge type="danger" text="OUTPUT" />

::: danger TO DO

Descrição.

:::

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`
- Padrão: `"0...0"`

## Usagem

```vhdl
REGISTER_1 : entity WORK.GENERIC_REGISTER
    generic map (
        DATA_WIDTH => 32
    )
    port map (
        clock       => clock,
        clear       => signal_clear,
        enable      => signal_enable,
        source      => signal_source,
        destination => signal_destination
    );
```

## Diagrama RTL

<pan-container>

![Diagrama de RTL do Registrador](/images/reference/components/generic_register_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_REGISTER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_REGISTER.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_REGISTER.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_GENERIC_REGISTER_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do Registrador](/images/reference/components/tb_generic_register_case_1.svg){.w-full .dark-invert}

</pan-container>
