---
outline: 2
---

# Flip Flop

[<Badge type="tip" text="GENERIC_FLIP_FLOP.vhd &boxbox;" />](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_FLIP_FLOP.vhd)

## Topologia

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

![Diagrama de RTL do Flip Flop](/images/referencia/componentes/generic_flip_flop_netlist.svg){.w-full .dark-invert}

## Casos de teste

[<Badge type="tip" text="test_GENERIC_FLIP_FLOP.py &boxbox;" />](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_FLIP_FLOP.py)

### Caso 1 <Badge type="info" text="tb_generic_flip_flop_case_1" />

Lógica sequencial:

![Forma de onda do caso de teste 1 do Flip Flop](/images/referencia/componentes/tb_generic_flip_flop_case_1.svg){.w-full .dark-invert}
