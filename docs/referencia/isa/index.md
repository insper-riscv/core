---
outline: [2, 3]
---

# Conjunto de Instruções

## Sintaxe

As instruções são vetores binários de 32 bits. Cada tipo de instrução reserva
sua sintaxe seguindo os segmentos:

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31</th>
            <th style="text-align: center; white-space: nowrap;">30 - 25</th>
            <th style="text-align: center; white-space: nowrap;">24 - 21</th>
            <th style="text-align: center; white-space: nowrap;">20</th>
            <th style="text-align: center; white-space: nowrap;">19 - 15</th>
            <th style="text-align: center; white-space: nowrap;">14 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11 - 8</th>
            <th style="text-align: center; white-space: nowrap;">8 - 7</th>
            <th style="text-align: center; white-space: nowrap;">6 - 0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">
                R
            </td>
            <td style="text-align: center;" colspan="2">
                funct7
            </td>
            <td style="text-align: center;" colspan="2">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                funct3
            </td>
            <td style="text-align: center;" colspan="2">
                rd
            </td>
            <td style="text-align: center;">
                opcode
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">
                I
            </td>
            <td style="text-align: center;">
                imm[31:11]
            </td>
            <td style="text-align: center;" colspan="3">
                imm[10:0]
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                funct3
            </td>
            <td style="text-align: center;" colspan="2">
                rd
            </td>
            <td style="text-align: center;">
                opcode
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">
                S
            </td>
            <td style="text-align: center;">
                imm[31:11]
            </td>
            <td style="text-align: center;">
                imm[10:5]
            </td>
            <td style="text-align: center;" colspan="2">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                funct3
            </td>
            <td style="text-align: center;" colspan="2">
                imm[4:0]
            </td>
            <td style="text-align: center;">
                opcode
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">
                B
            </td>
            <td style="text-align: center;">
                imm[31:12]
            </td>
            <td style="text-align: center;">
                imm[10:5]
            </td>
            <td style="text-align: center;" colspan="2">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                funct3
            </td>
            <td style="text-align: center;">
                imm[4:1]
            </td>
            <td style="text-align: center;">
                imm[11]
            </td>
            <td style="text-align: center;">
                opcode
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">
                U
            </td>
            <td style="text-align: center;" colspan="6">
                imm[31:12]
            </td>
            <td style="text-align: center;" colspan="2">
                rd
            </td>
            <td style="text-align: center;">
                opcode
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">
                J
            </td>
            <td style="text-align: center;">
                imm[31:20]
            </td>
            <td style="text-align: center;" colspan="2">
                imm[10:1]
            </td>
            <td style="text-align: center;">
                imm[11]
            </td>
            <td style="text-align: center;" colspan="2">
                imm[19:12]
            </td>
            <td style="text-align: center;" colspan="2">
                rd
            </td>
            <td style="text-align: center;">
                opcode
            </td>
        </tr>
    </tbody>
</table>

Sendo, para cada segmento:

- `opcode`: Codifica o tipo de instrução ou uma instrução específica;
- `funct3`: Codifica a operacionalização da instrução;
- `funct7`: Codifica uma variação da operacionalização;
- `rs1`: Endereça registrador de recurso primário;
- `rs2`: Endereça registrador de recurso secundário;
- `rd`: Endereça registrador de destinação;
- `imm`: Vetor do imediato.

### Opcode

Opcodes são segmentos de 7 bits do vetor de instrução. Cada tipo de instrução
possui um opcode ou uma instrução possui um opcode exclusivo. Para alguns tipos
de instrução, são codificados com mais de um opcode, seguindo a seguinte
generalização:

|    None    |   valor   |
| :--------: | :-------: |
|     OP     | `0110011` |
|   OP-IMM   | `0010011` |
|   STORE    | `0100011` |
|    LOAD    | `0000011` |
|   BRANCH   | `1100011` |
| **Outros** | `XXXXX11` |

### Imediato

Os imediatos são vetores binários de 32 bits. Cada tipo de instrução com
imediato possui uma sintaxe seguindo os segmentos:

<table>
    <thead>
        <tr>
            <th style="text-align: center;\f">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31</th>
            <th style="text-align: center; white-space: nowrap;">30 - 20</th>
            <th style="text-align: center; white-space: nowrap;">19 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11</th>
            <th style="text-align: center; white-space: nowrap;">10 - 5</th>
            <th style="text-align: center; white-space: nowrap;">4 - 1</th>
            <th style="text-align: center; white-space: nowrap;">0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">I</td>
            <td style="text-align: center;" colspan="4">inst[31]</td>
            <td style="text-align: center;" colspan="3">inst[30:20]</td>
        </tr>
        <tr>
            <td style="text-align: center;">S</td>
            <td style="text-align: center;" colspan="4">inst[31]</td>
            <td style="text-align: center;">inst[30:25]</td>
            <td style="text-align: center;" colspan="2">inst[11:7]</td>
        </tr>
        <tr>
            <td style="text-align: center;">B</td>
            <td style="text-align: center;" colspan="3">inst[31]</td>
            <td style="text-align: center;">inst[7]</td>
            <td style="text-align: center;">inst[30:25]</td>
            <td style="text-align: center;">inst[11:8]</td>
            <td style="text-align: center;"><code>0</code></td>
        </tr>
        <tr>
            <td style="text-align: center;">U</td>
            <td style="text-align: center;" colspan="3">inst[31:12]</td>
            <td style="text-align: center;" colspan="4"><code>0...0</code></td>
        </tr>
        <tr>
            <td style="text-align: center;">J</td>
            <td style="text-align: center;" colspan="2">inst[31]</td>
            <td style="text-align: center;">inst[19:12]</td>
            <td style="text-align: center;">inst[20]</td>
            <td style="text-align: center;" colspan="2">inst[30:21]</td>
            <td style="text-align: center;"><code>0</code></td>
        </tr>
    </tbody>
</table>

Sendo, para cada segmento, `inst` o vetor da instrução.

## Build

---

### `LUI` <Badge type="info" text="RV32I Base" />

Load Upper Immediate (Carregar Superior Imediato).

Carrega constantes de 32 bits. `LUI` coloca o valor imediato nos 20 bits
superiores do registrador `rd`, preenchendo os 12 bits mais baixos com zeros.

#### Sintaxe

| Tipo |   31-12    |    11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: |
|  U   | imm[31:12] | rd[x1-x31] | `0110111` |

#### Formato

`lui rd, imm`

#### Implementação

`x[rd] = imm[31:12] << 12`

---

### `AUIPC` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

## Shift

---

### `SLL` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SLLI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SRL` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SRLI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SRA` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SRAI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

## Arithmetic

### `ADD` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `ADDI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SUB` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `MUL` <Badge type="tip" text="“M” Standard Extension" />

::: danger TO DO

Work in progress.

:::

---

### `MULH` <Badge type="tip" text="“M” Standard Extension" />

::: danger TO DO

Work in progress.

:::

---

### `MULHSU` <Badge type="tip" text="“M” Standard Extension" />

::: danger TO DO

Work in progress.

:::

---

### `MULHU` <Badge type="tip" text="“M” Standard Extension" />

::: danger TO DO

Work in progress.

:::

---

### `DIV` <Badge type="tip" text="“M” Standard Extension" />

::: danger TO DO

Work in progress.

:::

---

### `DIVU` <Badge type="tip" text="“M” Standard Extension" />

::: danger TO DO

Work in progress.

:::

---

### `REM` <Badge type="tip" text="“M” Standard Extension" />

::: danger TO DO

Work in progress.

:::

---

### `REMU` <Badge type="tip" text="“M” Standard Extension" />

::: danger TO DO

Work in progress.

:::

---

## Logical

### `XOR` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `XORI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `OR` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `ORI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `AND` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `ANDI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

## Compare

### `SLT` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SLTI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SLTU` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SLTI` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

## Branch

### `BEQ` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `BNE` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `BLT` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `BGE` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `BLTU` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `BGEU` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

## Link

### `JAL` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `JALR` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

## Loads

### `LB` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `LH` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `LBU` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `LHU` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `LW` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

## Stores

### `SB` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SH` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::

---

### `SW` <Badge type="info" text="RV32I Base" />

::: danger TO DO

Work in progress.

:::
