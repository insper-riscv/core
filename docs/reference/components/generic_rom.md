---
outline: 2
---

# ROM

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_ROM.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_ROM.vhd &boxbox;" /></a>

<<< @/../src/TOP_LEVEL.vhd{vhdl:line-numbers}

:::

## Topologia

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
flowchart LR
    subgraph TOP ["GENERIC_ROM"]
        direction LR
        subgraph GENERIC ["generic map"]
            direction LR
            DATA_WIDTH
            ADDRESS_WIDTH
            ADDRESSABLE_WIDTH
        end
        C[("ROM")]
        style C scale:2
    end
    A([address]) -- ADDRESS_WIDTH ---> TOP
    TOP -- DATA_WIDTH ---> B([destination])
```

## Interface genérica

### `DATA_WIDTH` <Badge type="tip" text="GENERIC" />

Largura dos vetores de dados `source` e `destination`.

- Tipo: `natural`
- Padrão: `XLEN` (constante externa)

### `ADDRESS_WIDTH` <Badge type="tip" text="GENERIC" />

Largura do vetor da entrada `address`.

- Tipo: `natural`
- Padrão: `XLEN` (constante externa)

### `ADDRESSABLE_WIDTH` <Badge type="tip" text="GENERIC" />

Largura do vetor de endereçamento com mapeamento na memória.

- Tipo: `natural`
- Padrão: `10`

::: warning ATENÇÃO!

Deve ser menor ou igual a `ADDRESS_WIDTH`.

:::

## Interface de portas

### `address` <Badge type="warning" text="INPUT" />

Entrada de endereço da memória.

- Tipo: `std_logic_vector`
- Largura: variável `(ADDRESS_WIDTH - 1) downto 0`

### `destination` <Badge type="danger" text="OUTPUT" />

Saída de dados assumindo valor armazenado no endereço em `address`. Caso seja
endereçado um valor fora da largura mapeada assume sinal lógico baixo `"0...0"`

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`

## Usagem

```vhdl
ROM : entity WORK.GENERIC_ROM
    generic map (
        DATA_WIDTH_0      => 32;
        ADDRESS_WIDTH     => 32;
        ADDRESSABLE_WIDTH => 8
    )
    port map (
        source       => signal_source,
        destination  => signal_destination
    );
```

## DiagROMa RTL

![Diagrama de RTL da ROM](/images/reference/components/generic_rom_netlist.svg){.w-full .dark-invert}

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ROM.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_ROM.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_ADDER.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_GENERIC_ROM_case_1" />

Forma de onda:

![Forma de onda do caso de teste 1 da ROM](/images/reference/components/tb_generic_rom_case_1.svg){.w-full .dark-invert}
