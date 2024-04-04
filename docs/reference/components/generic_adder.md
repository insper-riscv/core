---
outline: 2
---

# Somador

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_ADDER.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_ADDER.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_ADDER.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_ADDER"]
        direction LR
        subgraph GENERIC ["generic map"]
            direction LR
            DATA_WIDTH
            DEFAULT_SOURCE_2
        end
        D(("ADDER"))
        style D scale:1.5
    end
    A([source_1]) -- DATA_WIDTH ---> TOP
    B([source_2]) -- DATA_WIDTH ---> TOP
    TOP -- DATA_WIDTH ---> C([destination])
```

</pan-container>

## Interface genérica

### `DATA_WIDTH` <Badge type="tip" text="GENERIC" />

Largura dos vetores de entrada e saída de dados.

- Tipo: `natural`
- Padrão: `XLEN` (constante externa)

### `DEFAULT_SOURCE_2` <Badge type="tip" text="GENERIC" />

Valor padrão de incremento. Dispensa necessidade de atribuir entrada `source_2`.

- Tipo: `integer`
- Padrão: `1`

## Interface de portas

### `source_1` <Badge type="warning" text="INPUT" />

Vetor de entrada primário.

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`

### `source_2` <Badge type="warning" text="INPUT" />

Vetor de entrada secundário.

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`
- Padrão: `to_signed(DEFAULT_SOURCE_2, DATA_WIDTH)`

### `destination` <Badge type="danger" text="OUTPUT" />

Saída de dados com o resultado de `source_1 + source_2`.

- Tipo: `std_logic_vector`
- Largura: `(DATA_WIDTH - 1) downto 0`

## Usagem

### Incremento constante

```vhdl
CONSTANT_ADDER : entity WORK.GENERIC_ADDER
    generic map (
        DATA_WIDTH_0     => 32,
        DEFAULT_SOURCE_2 => 1
    )
    port map (
        source_1    => signal_source_1,
        destination => signal_destination
    );
```

### Somador

```vhdl
ADDER : entity WORK.GENERIC_ADDER
    generic map (
        DATA_WIDTH_0 => 32
    )
    port map (
        source_1    => signal_source_1,
        source_2    => signal_source_2,
        destination => signal_destination
    );
```

## Diagrama RTL

<pan-container>

![Diagrama de RTL do somador](/images/reference/components/generic_adder_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ADDER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_ADDER.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_GENERIC_ADDER_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do somador](/images/reference/components/tb_generic_adder_case_1.svg){.w-full .dark-invert}

</pan-container>
