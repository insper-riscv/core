---
outline: 2
---

# Detector de Borda

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_EDGE_DETECTOR.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_EDGE_DETECTOR.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_EDGE_DETECTOR.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_EDGE_DETECTOR"]
        direction LR
        subgraph GENERIC ["generic map"]
            _[" "]
        end
        F[("private state_1\nprivate state_2")]
        style F scale:1.2
    end
    A(((clock))) ---> TOP
    C([source]) ---> TOP
    TOP ---> D([pulse])
```

</pan-container>

## Interface de portas

### `clock` <Badge type="warning" text="INPUT" />

Entrada do sinal de clock.

- Tipo: `std_logic`

### `source` <Badge type="warning" text="INPUT" />

Sinal de entrada com ruído.

- Tipo: `std_logic`

### `pulse` <Badge type="danger" text="OUTPUT" />

Sinal de borda sincronizada com `clock`.

- Tipo: `std_logic`

## Usagem

### Detector de borda de subida

```vhdl
EDGE_RAISE_DETECTOR : entity WORK.GENERIC_EDGE_DETECTOR(RISING_DETECTOR)
    Port map (
        clock  => clock,
        source => signal_source,
        pulse  => signal_pulse
    );
```

### Detector de borda de descida

```vhdl
EDGE_FALL_DETECTOR : entity WORK.GENERIC_EDGE_DETECTOR(FALLING_DETECTOR)
    Port map (
        clock  => signal_clock,
        source => signal_source,
        pulse  => signal_pulse
    );
```

## Diagrama RTL

<pan-container>

![Diagrama de RTL do detector de borda](/images/reference/components/generic_edge_detector_netlist.svg){.w-full .dark-invert}

</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_EDGE_DETECTOR.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_EDGE_DETECTOR.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_EDGE_DETECTOR.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_generic_edge_detector_case_1" />

Forma de onda:

<pan-container :grid="false">

![Caso de teste 1 do Detector de Borda](/images/reference/components/tb_generic_edge_detector_case_1.svg){.w-full .dark-invert}

### Caso 2 <Badge type="info" text="tb_generic_edge_detector_case_2" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 2 do Detector de Borda](/images/reference/components/tb_generic_edge_detector_case_2.svg){.w-full .dark-invert}

</pan-container>
