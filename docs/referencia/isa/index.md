---
outline: [2, 3]
---

# Conjunto de Instruções

As instruções são vetores binários de 32 bits. Cada tipo de instrução reserva
sua sintaxe seguindo os segmentos:

- `opcode`: Codifica o tipo de instrução ou uma instrução específica;
- `funct3`: Codifica a operacionalização da instrução;
- `funct7`: Codifica uma variação da operacionalização;
- `rs1`: Endereça registrador de recurso primário;
- `rs2`: Endereça registrador de recurso secundário;
- `rd`: Endereça registrador de destinação;
- `imm`: Vetor do imediato.

## Sintaxe

<table>
    <thead>
        <tr>
            <th style="text-align: center;">Tipo</th>
            <th style="text-align: center;">31</th>
            <th style="text-align: center;">30 - 25</th>
            <th style="text-align: center;">24 - 21</th>
            <th style="text-align: center;">20</th>
            <th style="text-align: center;">19 - 15</th>
            <th style="text-align: center;">14 - 12</th>
            <th style="text-align: center;">11 - 8</th>
            <th style="text-align: center;">8 - 7</th>
            <th style="text-align: center;">6 - 0</th>
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
            <td style="text-align: center;" colspan="4">
                imm
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
            <td style="text-align: center;" colspan="2">
                imm[11:5]
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
                imm[12]
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
                imm[20]
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

## Imediatos

Os imediatos são vetores binários de 32 bits. Cada tipo de instrução com
imediato possui uma sintaxe própria. Sendo:

- `inst`: Vetor da instrução.

<table>
    <thead>
        <tr>
            <th style="text-align: center;">Tipo</th>
            <th style="text-align: center;">31</th>
            <th style="text-align: center;">30 - 20</th>
            <th style="text-align: center;">19 - 12</th>
            <th style="text-align: center;">11</th>
            <th style="text-align: center;">10 - 5</th>
            <th style="text-align: center;">4 - 1</th>
            <th style="text-align: center;">0</th>
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
            <td style="text-align: center;">0</td>
        </tr>
        <tr>
            <td style="text-align: center;">U</td>
            <td style="text-align: center;" colspan="3">inst[31:12]</td>
            <td style="text-align: center;" colspan="4">0</td>
        </tr>
        <tr>
            <td style="text-align: center;">J</td>
            <td style="text-align: center;" colspan="2">inst[31]</td>
            <td style="text-align: center;">inst[19:12]</td>
            <td style="text-align: center;">inst[20]</td>
            <td style="text-align: center;" colspan="2">inst[30:21]</td>
            <td style="text-align: center;">0</td>
        </tr>
    </tbody>
</table>

## Opcodes

Opcodes são vetores binários de 7 bits. Cada tipo de instrução possui um opcode
ou uma instrução possui um opcode exclusivo.

|    None     |   valor   |
| :---------: | :-------: |
|     OP      | `0110011` |
|   OP-IMM    | `0010011` |
|    STORE    | `0100011` |
|    LOAD     | `0000011` |
|   BRANCH    | `1100011` |
|     LUI     | `0110111` |
|    AUIPC    | `0010111` |
|     JAL     | `1101111` |
|    JALR     | `1100111` |

## Build

---

### `LUI`

Load Upper Immediate (Carregar Superior Imediato).

Carrega constantes de 32 bits. `LUI` coloca o valor imediato nos 20 bits
superiores do registrador `rd`, preenchendo os 12 bits mais baixos com zeros.

#### Sintaxe

| Tipo |   31-12    | 11-7 |      6-0      |
| :--: | :--------: | :--: | :-----------: |
|  U   | imm[31:12] |  rd  | LUI (0110111) |

#### Formato

`lui rd, imm`

#### Implementação

`x[rd] = imm[31:12] << 12`

---

### `AUIPC`

::: danger TO DO

Work in progress.

:::

## Shift

---

### `SLL`

::: danger TO DO

Work in progress.

:::

---

### `SLLI`

::: danger TO DO

Work in progress.

:::

---

### `SRL`

::: danger TO DO

Work in progress.

:::

---

### `SRLI`

::: danger TO DO

Work in progress.

:::

---

### `SRA`

::: danger TO DO

Work in progress.

:::

---

### `SRAI`

::: danger TO DO

Work in progress.

:::

---

## Arithmetic

### `ADD`

::: danger TO DO

Work in progress.

:::

---

### `ADDI`

::: danger TO DO

Work in progress.

:::

---

### `SUB`

::: danger TO DO

Work in progress.

:::

---

### `MUL`

::: danger TO DO

Work in progress.

:::

---

### `MULH`

::: danger TO DO

Work in progress.

:::

---

### `MULHSU`

::: danger TO DO

Work in progress.

:::

---

### `MULHU`

::: danger TO DO

Work in progress.

:::

---

### `DIV`

::: danger TO DO

Work in progress.

:::

---

### `DIVU`

::: danger TO DO

Work in progress.

:::

---

### `REM`

::: danger TO DO

Work in progress.

:::

---

### `REMU`

::: danger TO DO

Work in progress.

:::

---

## Logical

### `XOR`

::: danger TO DO

Work in progress.

:::

---

### `XORI`

::: danger TO DO

Work in progress.

:::

---

### `OR`

::: danger TO DO

Work in progress.

:::

---

### `ORI`

::: danger TO DO

Work in progress.

:::

---

### `AND`

::: danger TO DO

Work in progress.

:::

---

### `ANDI`

::: danger TO DO

Work in progress.

:::

---

## Compare

### `SLT`

::: danger TO DO

Work in progress.

:::

---

### `SLTI`

::: danger TO DO

Work in progress.

:::

---

### `SLTU`

::: danger TO DO

Work in progress.

:::

---

### `SLTI`

::: danger TO DO

Work in progress.

:::

---

## Branch

### `BEQ`

::: danger TO DO

Work in progress.

:::

---

### `BNE`

::: danger TO DO

Work in progress.

:::

---

### `BLT`

::: danger TO DO

Work in progress.

:::

---

### `BGE`

::: danger TO DO

Work in progress.

:::

---

### `BLTU`

::: danger TO DO

Work in progress.

:::

---

### `BGEU`

::: danger TO DO

Work in progress.

:::

---

## Link

### `JAL`

::: danger TO DO

Work in progress.

:::

---

### `JALR`

::: danger TO DO

Work in progress.

:::

---

## Loads

### `LB`

::: danger TO DO

Work in progress.

:::

---

### `LH`

::: danger TO DO

Work in progress.

:::

---

### `LBU`

::: danger TO DO

Work in progress.

:::

---

### `LHU`

::: danger TO DO

Work in progress.

:::

---

### `LW`

::: danger TO DO

Work in progress.

:::

---

## Stores

### `SB`

::: danger TO DO

Work in progress.

:::

---

### `SH`

::: danger TO DO

Work in progress.

:::

---

### `SW`

::: danger TO DO

Work in progress.

:::
