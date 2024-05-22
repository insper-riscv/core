---
outline: 2
---

# RAM

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/src/GENERIC_RAM.vhd" target="blank" style="float:right"><Badge type="tip" text="GENERIC_RAM.vhd &boxbox;" /></a>

<<< @/../src/GENERIC_RAM.vhd{vhdl:line-numbers}

:::

## Topologia

<pan-container selector=".mermaid">

<!--@include: @/.includes/generic_ram-topology.md-->

</pan-container>

## Interface genérica

### `DATA_WIDTH` <Badge type="neutral" text="GENERIC" />

Largura dos vetores de dados `source` e `destination`.

- Tipo: `natural`
- Padrão: `8`

### `ADDRESS_WIDTH` <Badge type="neutral" text="GENERIC" />

Largura do vetor da entrada `address`.

- Tipo: `natural`
- Padrão: `8`

### `ADDRESSABLE_WIDTH` <Badge type="neutral" text="GENERIC" />

Largura do vetor de endereçamento com mapeamento na memória.

- Tipo: `natural`
- Padrão: `7`

::: warning ATENÇÃO!

Deve ser menor ou igual a `ADDRESS_WIDTH`.

:::

## Interface de portas

### `clock` <Badge type="success" text="INPUT" />

Entrada do sinal de clock.

- Tipo: `std_logic`

### `enable` <Badge type="success" text="INPUT" />

Entrada do sinal habilitação do uso da memória para leitura ou escrita.

- Tipo: `std_logic`

### `enable_read` <Badge type="success" text="INPUT" />

Entrada do sinal habilitação da leitura da memória. Saída `destination` assume
sinal de alta impedância caso `enable_read = '0'`.

- Tipo: `std_logic`

### `enable_write` <Badge type="success" text="INPUT" />

Entrada do sinal habilitação da escrina da memória.

- Tipo: `std_logic`

### `address` <Badge type="success" text="INPUT" />

Entrada de endereço da memória.

- Tipo: `std_logic_vector`
- Largura: variável `(ADDRESS_WIDTH - 1) downto 0`

### `source` <Badge type="success" text="INPUT" />

Entrada de dados.

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`

### `destination` <Badge type="danger" text="OUTPUT" />

Saída de dados assumindo valor armazenado no endereço em `address`. Caso seja
endereçado um valor fora da largura mapeada assume sinal lógico baixo `"0...0"`

- Tipo: `std_logic_vector`
- Largura: variável `(DATA_WIDTH - 1) downto 0`

## Usagem

```vhdl
RAM : entity WORK.GENERIC_RAM
    generic map (
        DATA_WIDTH_0      => 32;
        ADDRESS_WIDTH     => 32;
        ADDRESSABLE_WIDTH => 8
    )
    port map (
        clock        => clock,
        enable       => signal_enable,
        enable_read  => signal_enable_read,
        enable_write => signal_enable_write,
        address      => signal_address,
        source       => signal_source,
        destination  => signal_destination
    );
```

## Diagrama RTL

<pan-container>

![Diagrama de RTL da RAM](/images/reference/components/generic_ram_netlist.svg){.w-full .dark-invert}
</pan-container>

## Casos de teste

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_RAM.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_RAM.py &boxbox;" /></a>

<<< @/../test/test_GENERIC_RAM.py{py:line-numbers}

:::

### Caso 1 <Badge type="info" text="tb_GENERIC_RAM_case_1" />

Forma de onda:

<pan-container :grid="false">

![Forma de onda do caso de teste 1 da RAM](/images/reference/components/tb_generic_ram_case_1.svg){.w-full .dark-invert}

</pan-container>
