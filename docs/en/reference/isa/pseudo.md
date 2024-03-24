---
outline: 2
---

# Pseudo-instructions

Pseudo-instructions are instructions that exist in assembly language 
but do not exist in the processor's instruction set architecture. 
The assembler maps pseudo-instructions into processor instructions.

## `la` (non-PIC)

Load Absolute Address.

Where `delta` = `symbol - pc`.

### Format

`la rd, symbol`

### Implementation

`x[rd] = pc + imm(U) + imm(I)`

### Base Instructions

```asm
auipc rd, delta[31:12] + delta[11]
addi rd, rd, delta[11:0]
```

## `la` (PIC)

::: danger TO DO

Work in progress.

:::

## `lla`

::: danger TO DO

Work in progress.

:::

## `l{b|h|w|d}`

::: danger TO DO

Work in progress.

:::

## `s{b|h|w|d}`

::: danger TO DO

Work in progress.

:::

---

## `nop`

::: danger TO DO

Work in progress.

:::

## `li`

::: danger TO DO

Work in progress.

:::

## `mv`

::: danger TO DO

Work in progress.

:::

## `not`

::: danger TO DO

Work in progress.

:::

## `neg`

::: danger TO DO

Work in progress.

:::

## `negw`

::: danger TO DO

Work in progress.

:::

## `seqz`

::: danger TO DO

Work in progress.

:::

## `snez`

::: danger TO DO

Work in progress.

:::

## `sltz`

::: danger TO DO

Work in progress.

:::

## `sgtz`

::: danger TO DO

Work in progress.

:::

---

## `beqz`

::: danger TO DO

Work in progress.

:::

## `bnez`

::: danger TO DO

Work in progress.

:::

## `blez`

::: danger TO DO

Work in progress.

:::

## `bgez`

::: danger TO DO

Work in progress.

:::

## `bltz`

::: danger TO DO

Work in progress.

:::

## `bgtz`

::: danger TO DO

Work in progress.

:::

---

## `bgt`

::: danger TO DO

Work in progress.

:::

## `ble`

::: danger TO DO

Work in progress.

:::

## `bgtu`

::: danger TO DO

Work in progress.

:::

## `bleu`

::: danger TO DO

Work in progress.

:::

---

## `j`

::: danger TO DO

Work in progress.

:::

## `jal offset`

::: danger TO DO

Work in progress.

:::

## `jr`

::: danger TO DO

Work in progress.

:::

## `jalr rs`

::: danger TO DO

Work in progress.

:::

## `ret`

::: danger TO DO

Work in progress.

:::

## `call`

::: danger TO DO

Work in progress.

:::

## `tail`

::: danger TO DO

Work in progress.

:::

---

## `fence`

::: danger TO DO

Work in progress.

:::
