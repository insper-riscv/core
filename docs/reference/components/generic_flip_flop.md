---
outline: 2
---

# Flip Flop

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_FLIP_FLOP.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_FLIP_FLOP.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_FLIP_FLOP.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_FLIP_FLOP"]
        direction LR
        subgraph GENERIC ["generic map"]
            _[" "]
        end
        F[("state")]
        style F scale:1.2
    end
    A(((clock))) ---> TOP
    B([clear]) ---> TOP
    C([enable]) ---> TOP
    D([source]) ---> TOP
    TOP ---> E([state])
```

</pan-container>

## Interface de portas

### `clock` <Badge type="warning" text="INPUT" />

Entrada do sinal de clock.

- Tipo: `std_logic`

### `clear` <Badge type="warning" text="INPUT" />

::: danger TO DO

Descrição.

:::

- tipo: `std_logic`

### `enable` <Badge type="warning" text="INPUT" />

::: danger TO DO

Descrição.

:::

- tipo: `std_logic`

### `source` <Badge type="warning" text="INPUT" />

::: danger TO DO

Descrição.

:::

- tipo: `std_logic`

### `state` <Badge type="danger" text="OUTPUT" />

::: danger TO DO

Escrever descrição state

:::

- tipo: `std_logic`
- padrão: `0`

## Usagem

```vhdl
FLIP_FLOP_1 : entity WORK.GENERIC_FLIP_FLOP
    port map (
        clock  => clock,
        clear  => signal_clear,
        enable => signal_enable,
        source => signal_source,
        state  => signal_state
    );
```

## Diagrama RTL

<pan-container>

![Diagrama de RTL do Flip Flop](/images/reference/components/generic_flip_flop_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_FLIP_FLOP.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_FLIP_FLOP.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_FLIP_FLOP.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_generic_flip_flop_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 do Flip Flop](/images/reference/components/tb_generic_flip_flop_case_1.svg){.w-full .dark-invert}

</pan-container>
