---
outline: 2
---

# Contador

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_COUNTER.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_COUNTER.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_COUNTER.vhd{vhdl:line-numbers}

:::

## Topology

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_COUNTER"]
        direction LR
        subgraph GENERIC ["generic map"]
            direction LR
            DEFAULT_OVERFLOW
        end
        F[("overflow\ncount\nstate")]
        style F scale:1.3
    end
    A(((clock))) ---> TOP
    B([clear]) ---> TOP
    C([update]) ---> TOP
    D([source]) -- 5 ---> TOP
    TOP ---> E([state])
```

## Generic interface

### `DEFAULT_OVERFLOW` <Badge type="tip" text="GENERIC" />

Valor Padrão de overflow.

- Type: `natural`
- Default: `CLOCK_FREQUENCY` (external constant)

## Port interface

### `clock` <Badge type="warning" text="INPUT" />

Entrada do sinal de clock.

- Type: `std_logic`

### `clear` <Badge type="warning" text="INPUT" />

Atribui a saída `state` para sinal lógico baixo. Não reinicia a contagem.

- Type: `std_logic`

### `update` <Badge type="warning" text="INPUT" />

Entrada do signal de limpeza do estado do contador. Reinicia a contagem mas não
limpa o estado do contador.

- Type: `std_logic`
- Default: `'0'`

### `source` <Badge type="warning" text="INPUT" />

Valor `n` de estouro da contagem. A cada `2^n` ciclos de clock, atribui a saída
`state` para sinal lógico alto.

- Type: `std_logic_vector`
- Width: 5 bits `4 downto 0`
- Default: `DEFAULT_OVERFLOW`

### `state` <Badge type="danger" text="OUTPUT" />

Estado do contador. Nível lógico alto caso tenha ultrapassado a contagem de
ciclos definida.

- Type: `std_logic`
- Default: `0`

## Usage

### Base de tempo constante

```vhdl
TIMER_COUNTER : entity WORK.GENERIC_COUNTER
    generic map (
        DEFAULT_OVERFLOW => 50_000_000 -- Valor da frequência do clock, equivalente a contagem de 1 segundo
    )
    port map (
        clock  => clock,
        clear  => signal_clear,
        state  => signal_state
    );
```

### Base de tempo variável

```vhdl
TIMER_COUNTER : entity WORK.GENERIC_COUNTER
    port map (
        clock  => clock,
        clear  => signal_clear,
        update => signal_update,
        source => signal_source,
        state  => signal_state
    );
```

## RTL View

![RTL view from contador](/images/reference/components/generic_counter_netlist.svg){.w-full .dark-invert}

## Test cases

::: details Source <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_COUNTER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_COUNTER.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

### Case 1 <Badge type="info" text="tb_GENERIC_COUNTER_case_1" />

Waveform:

![Waveform from caso de teste 1 do contador](/images/reference/components/tb_generic_counter_case_1.svg){.w-full .dark-invert}
