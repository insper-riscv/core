---
outline: 2
---

# Debounce

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_DEBOUNCE.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_DEBOUNCE.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_DEBOUNCE.vhd{vhdl:line-numbers}

:::

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_DEBOUNCE"]
        direction LR
        subgraph GENERIC ["generic map"]
            direction LR
            DEFAULT_OVERFLOW
        end
        E["EDGE_DETECTOR"]
        click E href "./generic_edge_detector.html"
        F[("state")]
        style F scale:1.3
        click F href "./generic_flip_flop.html"
    end
    A(((clock))) ---> TOP
    B([clear]) ---> TOP
    C([source]) ---> TOP
    TOP ---> D([state])
```

## Interface de portas

### `clock` <Badge type="warning" text="INPUT" />

Entrada do sinal de clock.

- Tipo: `std_logic`

### `clear` <Badge type="warning" text="INPUT" />

Entrada que reseta o debounce.

- Tipo: `std_logic`
- Padrão: `'0'`

### `source` <Badge type="warning" text="INPUT" />

::: danger TO DO

```md
[DESCRIÇÃO]

- Tipo: `std_logic`
```

:::

### `state` <Badge type="danger" text="OUTPUT" />

::: danger TO DO

```md
[DESCRIÇÃO]

- Tipo: `std_logic`
- Padrão: `'0'`
```

:::

## Usagem

```vhdl
DEBOUNCE_1 : entity WORK.GENERIC_DEBOUNCE
    Port map (
        clock  => clock,
        clear  => signal_clear,
        source => signal_source,
        state  => signal_state
    );
```

## Diagrama RTL

![Diagrama de RTL do debounce](/images/reference/components/generic_debounce_netlist.svg){.w-full .dark-invert}

### Dependências

- `EDGE_DETECTOR`: [Detector de borda](./generic_edge_detector.html)
- `STATE_REGISTER`: [Flip Flop](./generic_flip_flop.html)

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_DEBOUNCE.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_DEBOUNCE.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

::: danger TO DO

```md
### Caso 1 <Badge type="info" text="tb_generic_debounce_case_1" />

Forma de onda:

![Forma de onda do caso de teste 1 do debounce](/images/reference/components/tb_generic_debounce_case_1.svg){.w-full .dark-invert}
```

:::
