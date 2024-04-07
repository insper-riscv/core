---
outline: 2
---

# Multiplexador 2x1

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_MUX_2X1.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_MUX_2X1.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_MUX_2X1.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_MUX_2X1"]
        direction LR
        subgraph GENERIC ["generic map"]
            direction LR
            DATA_WIDTH
        end
    end
    A([source_1]) -- DATA_WIDTH ---> TOP
    B([source_2]) -- DATA_WIDTH ---> TOP
    K([selector]) ---> TOP
    TOP -- DATA_WIDTH ---> D([destination])
  
```

</pan-container>

## Interface genérica

### `DATA_WIDTH` <Badge type="neutral" text="GENERIC" />

Largura dos vetores de entrada e saída de dados.

- Tipo: `natural`
- Padrão: `XLEN` (constante externa)

## Interface de portas

### `source_1` <Badge type="success" text="INPUT" />

Vetor de entrada primário. `destination <= source_1` se `selector = '0'`.

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`

### `source_2` <Badge type="success" text="INPUT" />

Vetor de entrada secundário. `destination <= source_2` se `selector = '1'`.

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`

### `selector` <Badge type="success" text="INPUT" />

Seleção do vetor de saída de `destination`.

- tipo: `std_logic`

### `destination` <Badge type="danger" text="OUTPUT" />

Vetor de saída.

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`

## Usagem

```vhdl
MUX_1 : entity WORK.GENERIC_MUX_2X1
    generic map (
        DATA_WIDTH_0 => 32
    )
    port map (
        source_1    => signal_source_1,
        source_2    => signal_source_2,
        selector    => signal_selector,
        destination => signal_destination
    );
```

## Diagrama RTL

<pan-container>

![Diagrama de RTL do mux 2x1](/images/reference/components/generic_mux_2x1_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_MUX_2X1.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_MUX_2X1.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_MUX_2X1.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_generic_mux_2x1_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do Flip Flop](/images/reference/components/tb_generic_mux_2x1_case_1.svg){.w-full .dark-invert}

</pan-container>
