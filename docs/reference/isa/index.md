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

---

## Carrega Constante

### `LUI` <Badge type="info" text="RV32I Base" />

Load Upper Immediate (Carregar Superior Imediato).

Carrega constantes de 32 bits. `LUI` coloca o valor imediato nos 20 bits
superiores do registrador `rd`, preenchendo os 12 bits mais baixos com zeros.

#### Sintaxe

| Tipo |   31-12    | 11-7 |    6-0    |
| :--: | :--------: | :--: | :-------: |
|  U   | imm[31:12] |  rd  | `0110111` |

#### Formato

`lui rd, imm`

#### Implementação

`x[rd] = imm[31:12] << 12`

---

### `AUIPC` <Badge type="info" text="RV32I Base" />

Add Upper Immediate (Adiciona Superior Imediato).

Desloca o valor do imediato 12 bits para a esquerda, preenchendo os 12 bits mais
baixos com zero e o adiciona ao PC. Escreve o resultado no registrador `rd`

#### Sintaxe

| Tipo |   31-12    | 11-7 |    6-0    |
| :--: | :--------: | :--: | :-------: |
|  U   | imm[31:12] |  rd  | `0010111` |

#### Formato

`auipc rd, imm`

#### Implementação

`x[rd] = pc + sext(imm[31:12] << 12)`

---

## Lógica Aritmética

### `ADD` <Badge type="info" text="RV32I Base" />

Add (Adição).

Soma os registradores `rs1` e `rs2` e armazena o resultado no registrador `rd`.
Em caso de overflow, ele é ignorado.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000000 |  rs2  |  rs1  |  000  |  rd  | OP  |

#### Formato

`add rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] + x[rs2]`

---

### `ADDI` <Badge type="info" text="RV32I Base" />

Add Immediate (Adição Imediata).

Soma o registrador `rs1` com o sinal estendido do imediato e armazena o
resultado no registrador `rd`. Em caso de overflow, ele é ignorado.

#### Sintaxe

| Tipo |   31-20   | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  000  |  rd  | OP-IMM |

#### Formato

`addi rd, rs1, immediate`

#### Implementação

`x[rd] = x[rs1] + sext(immediate)`

---

### `SUB` <Badge type="info" text="RV32I Base" />

Subtract (Subtração).

Subtrai o registrador `rs1` pelo `rs2` e armazena o resultado no registrador
`rd`. Em caso de overflow, ele é ignorado.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0100000 |  rs2  |  rs1  |  000  |  rd  | OP  |

#### Formato

`sub rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] - x[rs2]`

---

### `MUL` <Badge type="tip" text="“M” Standard Extension" />

Multiply (Multiplicação).

Multiplica os registradores `rs1` e `rs2` e armazena o resultado no registrador
`rd`. Em caso de overflow, ele é ignorado.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000001 |  rs2  |  rs1  |  000  |  rd  | OP  |

#### Formato

`mul rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] × x[rs2]`

---

### `MULH` <Badge type="tip" text="“M” Standard Extension" />

Multiply High (Multiplicação Superior).

Multiplica os registradores `rs1` e `rs2`, considerando que são números de
complemento de dois e armazena a metade superior do produto no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000001 |  rs2  |  rs1  |  001  |  rd  | OP  |

#### Formato

`mulh rd, rs1, rs2`

#### Implementação

`x[rd] = (x[rs1] × x[rs2]) >> XLEN`

---

### `MULHSU` <Badge type="tip" text="“M” Standard Extension" />

Multiply High Signed and Unsigned (Multiplicação Superior com Sinal e Sem
Sinal).

Multiplica os registradores `rs1` e `rs2`, considerando que `rs1` é um número de
complemento de dois e `rs2` é um número sem sinal, e armazena a metade superior
do produto no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000001 |  rs2  |  rs1  |  010  |  rd  | OP  |

#### Formato

`mulhsu rd, rs1, rs2`

#### Implementação

`x[rd] = (x[rs1] * x[rs2]) >> XLEN`

---

### `MULHU` <Badge type="tip" text="“M” Standard Extension" />

Multiply High Unsigned (Multiplicação Superior Sem Sinal).

Multiplica os registradores `rs1` e `rs2`, considerando que ambos são números
sem sinal, e armazena a metade superior do produto no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000001 |  rs2  |  rs1  |  011  |  rd  | OP  |

#### Formato

`mulhu rd, rs1, rs2`

#### Implementação

`x[rd] = (x[rs1] × x[rs2]) >> XLEN`

---

### `DIV` <Badge type="tip" text="“M” Standard Extension" />

Divide (Divisão).

Divide o registrador `rs1` por `rs2`, considerando que são números de
complemento de dois, arredondando para zero, e armazena o quociente no
registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000001 |  rs2  |  rs1  |  100  |  rd  | OP  |

#### Formato

`div rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] ÷ x[rs2]`

---

### `DIVU` <Badge type="tip" text="“M” Standard Extension" />

Divide Unsigned (Divisão Sem Sinal).

Divide o registrador `rs1` por `rs2`, considerando que são números sem sinal,
arredondando para zero, e armazena o quociente no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000001 |  rs2  |  rs1  |  101  |  rd  | OP  |

#### Formato

`div rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] ÷ x[rs2]`

---

### `REM` <Badge type="tip" text="“M” Standard Extension" />

Remainder (Resto).

Divide o registrador `rs1` por `rs2`, considerando que são números de
complemento de dois, arredondando para zero, e armazena o resto no registrador
`rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000001 |  rs2  |  rs1  |  110  |  rd  | OP  |

#### Formato

`rem rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] % x[rs2]`

---

### `REMU` <Badge type="tip" text="“M” Standard Extension" />

Remainder Unsigned (Resto Sem Sinal).

Divide o registrador `rs1` por `rs2`, considerando que são números sem sinal,
arredondando para zero, e armazena o resto no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000001 |  rs2  |  rs1  |  111  |  rd  | OP  |

#### Formato

`rem rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] % x[rs2]`

---

## Lógicas Booleana

### `XOR` <Badge type="info" text="RV32I Base" />

Exclusive OR (OU Exclusivo).

Realiza a operação lógica XOR, bit a bit, entre os registradores `rs1` e `rs2` e
armazena o resultado no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000000 |  rs2  |  rs1  |  100  |  rd  | OP  |

#### Formato

`xor rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] ˆ x[rs2]`

---

### `XORI` <Badge type="info" text="RV32I Base" />

Exclusive OR Immediate (OU Exclusivo Imediato).

Realiza a operação lógica XOR, bit a bit, entre o registrador `rs1` e o imediato
com sinal estendido e armazena o resultado no registrador `rd`.

#### Sintaxe

| Tipo |   31-20   | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  100  |  rd  | OP-IMM |

#### Formato

`xori rd, rs1, immediate`

#### Implementação

`x[rd] = x[rs1] ˆ sext(immediate)`

---

### `OR` <Badge type="info" text="RV32I Base" />

OR (OU).

Realiza a operação lógica OR, bit a bit, entre os registradores `rs1` e `rs2` e
armazena o resultado no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000000 |  rs2  |  rs1  |  110  |  rd  | OP  |

#### Formato

`or rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] | x[rs2]`

---

### `ORI` <Badge type="info" text="RV32I Base" />

OR Immediate (OU Imediato).

Realiza a operação lógica OR, bit a bit, entre o registrador `rs1` e o imediato
com sinal estendido e armazena o resultado no registrador `rd`.

#### Sintaxe

| Tipo |   31-20   | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  110  |  rd  | OP-IMM |

#### Formato

`ori rd, rs1, immediate`

#### Implementação

`x[rd] = x[rs1] | sext(immediate)`

---

### `AND` <Badge type="info" text="RV32I Base" />

AND (E).

Realiza a operação lógica AND, bit a bit, entre os registradores `rs1` e `rs2` e
armazena o resultado no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000000 |  rs2  |  rs1  |  111  |  rd  | OP  |

#### Formato

`and rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] & x[rs2]`

---

### `ANDI` <Badge type="info" text="RV32I Base" />

AND Immediate (E Imediato).

Realiza a operação lógica OR, bit a bit, entre o registrador `rs1` e o imediato
com sinal estendido e armazena o resultado no registrador `rd`.

#### Sintaxe

| Tipo |   31-20   | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  111  |  rd  | OP-IMM |

#### Formato

`andi rd, rs1, immediate`

#### Implementação

`x[rd] = x[rs1] & sext(immediate)`

---

## Operação de Deslocamento

### `SLL` <Badge type="info" text="RV32I Base" />

Shift Left Logical (Deslocamento à Esquerda Lógico).

Desloca o valor do registrador `rs1` à esquerda pelo número de posições indicado
pelos 5 bits menos significativos do valor do registrador `rs2`. Os bits
remanescentes de `rs2` são ignorados. Os bits vazios de `rs1` são preenchidos
com zeros. O resultado é escrito no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000000 |  rs2  |  rs1  |  001  |  rd  | OP  |

#### Formato

`sll rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] << x[rs2]`

---

### `SLLI` <Badge type="info" text="RV32I Base" />

Shift Left Logical Immediate (Deslocamento à Esquerda Lógico Imediato).

Desloca o valor do registrador `rs1` à esquerda pelo número de posições indicado
pelo `shamt`. Os bits vazios de `rs1` são preenchidos com zeros. O resultado é
escrito no registrador `rd`. Só é permitido quando `shamt[5] = 0`.

#### Sintaxe

| Tipo | 31-26  | 25-20 | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :----: | :---: | :---: | :---: | :--: | :----: |
|  I   | 000000 | shamt |  rs1  |  001  |  rd  | OP-IMM |

#### Formato

`slli rd, rs1, shamt`

#### Implementação

`x[rd] = x[rs1] << shamt`

---

### `SRL` <Badge type="info" text="RV32I Base" />

Shift Right Logical (Deslocamento à Direita Lógico).

Desloca o valor do registrador `rs1` à direita pelo número de posições indicado
pelos 5 bits menos significativos do valor do registrador `rs2`. Os bits
remanescentes de `rs2` são ignorados. Os bits vazios de `rs1` são preenchidos
com zeros. O resultado é escrito no registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000000 |  rs2  |  rs1  |  101  |  rd  | OP  |

#### Formato

`srl rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] >> x[rs2]`

---

### `SRLI` <Badge type="info" text="RV32I Base" />

Shift Right Logical Immediate (Deslocamento à Direita Lógico Imediato).

Desloca o valor do registrador `rs1` à direita pelo número de posições indicado
pelo `shamt`. Os bits vazios de `rs1` são preenchidos com zeros. O resultado é
escrito no registrador `rd`. Só é permitido quando `shamt[5] = 0`.

#### Sintaxe

| Tipo | 31-26  | 25-20 | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :----: | :---: | :---: | :---: | :--: | :----: |
|  I   | 000000 | shamt |  rs1  |  101  |  rd  | OP-IMM |

#### Formato

`srli rd, rs1, shamt`

#### Implementação

`x[rd] = x[rs1] >>shamt`

---

### `SRA` <Badge type="info" text="RV32I Base" />

Shift Right Arithmetic (Deslocamento à Direita Aritmético).

Desloca o valor do registrador `rs1` à direita pelo número de posições indicado
pelos 5 bits menos significativos do valor do registrador `rs2`. Os bits
remanescentes de `rs2` são ignorados. Os bits vazios de `rs1` são preenchidos
com cópias do bit mais significativo de `rs1`. O resultado é escrito no
registrador `rd`.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0100000 |  rs2  |  rs1  |  101  |  rd  | OP  |

#### Formato

`sra rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] >> x[rs2]`

---

### `SRAI` <Badge type="info" text="RV32I Base" />

Shift Right Arithmetic Immediate (Deslocamento à Direita Aritmético Imediato).

Desloca o valor do registrador `rs1` à direita pelo número de posições indicado
pelo `shamt`. Os bits vazios de `rs1` são preenchidos com cópias do bit mais
significativo de `rs1`. O resultado é escrito no registrador `rd`. Só é
permitido quando `shamt[5] = 0`.

#### Sintaxe

| Tipo | 31-26  | 25-20 | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :----: | :---: | :---: | :---: | :--: | :----: |
|  I   | 010000 | shamt |  rs1  |  101  |  rd  | OP-IMM |

#### Formato

`srai rd, rs1, shamt`

#### Implementação

`x[rd] = x[rs1] >> shamt`

---

## Comparação

### `SLT` <Badge type="info" text="RV32I Base" />

Set if Less Than (Definir se Menor que).

Verifica se o registrador `rs1` é menor que o registrador `rs2`, considerando
que são complemento de dois, em caso positivo, armazena 1 no registrador `rd`,
caso contrário, armazena 0.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000000 |  rs2  |  rs1  |  010  |  rd  | OP  |

#### Formato

`slt rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] < x[rs2]`

---

### `SLTI` <Badge type="info" text="RV32I Base" />

Set if Less Than Immediate (Definir se Menor que Imediato).

Verifica se o registrador `rs1` é menor que o imediato com extensão de sinal,
considerando que são complemento de dois, em caso positivo, armazena 1 no
registrador `rd`, caso contrário, armazena 0.

#### Sintaxe

| Tipo |   31-20   | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  010  |  rd  | OP-IMM |

#### Formato

`slti rd, rs1, immediate`

#### Implementação

`x[rd] = x[rs1] < sext(immediate)`

---

### `SLTIU` <Badge type="info" text="RV32I Base" />

Set if Less Than Immediate Unisgned(Definir se Menor que Imediato Sem Sinal).

Verifica se o registrador `rs1` é menor que o imediato com extensão de sinal,
considerando que são sem sinal, em caso positivo, armazena 1 no registrador
`rd`, caso contrário, armazena 0.

#### Sintaxe

| Tipo |   31-20   | 19-15 | 14-12 | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  011  |  rd  | OP-IMM |

#### Formato

`slti rd, rs1, immediate`

#### Implementação

`x[rd] = x[rs1] < sext(immediate)`

---

### `SLTU` <Badge type="info" text="RV32I Base" />

Set if Less Than Unsigned(Definir se Menor que Sem Sinal).

Verifica se o registrador `rs1` é menor que o registrador `rs2`, considerando
que são sem sinal, em caso positivo, armazena 1 no registrador `rd`, caso
contrário, armazena 0.

#### Sintaxe

| Tipo |  31-25  | 24-20 | 19-15 | 14-12 | 11-7 | 6-0 |
| :--: | :-----: | :---: | :---: | :---: | :--: | :-: |
|  R   | 0000000 |  rs2  |  rs1  |  011  |  rd  | OP  |

#### Formato

`sltu rd, rs1, rs2`

#### Implementação

`x[rd] = x[rs1] < x[rs2]`

---

## Desvio Incondicional

### `JAL` <Badge type="info" text="RV32I Base" />

Jump and Link (Salto e Link).

Escreve o endereço da próxima instrução (PC+4) no registrador `rd` e modifica o
PC para o valor atual somado ao offset com extensão de sinal. Se `rd` for
omitido, o valor de retorno é armazenado em `x1`.

#### Sintaxe

| Tipo |   31-12   | 11-7 | 6-0 |
| :--: | :-------: | :--: | :-: |
|  J   | offset[20 | 10:1 | 11  |

#### Formato

`jal rd, offset`

#### Implementação

`x[rd] = pc+4; pc += sext(offset)`

---

### `JALR` <Badge type="info" text="RV32I Base" />

Jump and Link Register (Salto e Link por Registrador).

Realiza um cópia do PC para `rs1 + sext(offset)`, mascara bit menos
significativo do endereço resultante e armazena o endereço anterior de PC+4 no
registrador `rd`. Se `rd` for omitido, o valor é armazenado em `x1`.

#### Sintaxe

| Tipo |    31-20     | 19-15 | 14-12 | 11-7 |    6-0    |
| :--: | :----------: | :---: | :---: | :--: | :-------: |
|  I   | offset[11:0] |  rs1  |  000  |  rd  | `1100111` |

#### Formato

`jalr rd, offset(rs1)`

#### Implementação

`t =pc+4; pc=(x[rs1]+sext(offset))&∼1; x[rd]=t`

---

## Desvio Condicional

### `BEQ` <Badge type="info" text="RV32I Base" />

Branch if Equal (Desvio se Igual)

Verifica se o registrador `rs1` é igual ao registrador `rs2`, em caso positivo,
modifica o PC para o valor atual somado ao offset com extensão de sinal.

#### Sintaxe

| Tipo |   31-25   | 24-20 | 19-15 | 14-12 | 11-7 |    6-0     |
| :--: | :-------: | :---: | :---: | :---: | :--: | :--------: |
|  B   | offset[12 | 10:5] |  rs2  |  rs1  | 000  | offset[4:1 |

#### Formato

`beq rs1, rs2, offset`

#### Implementação

`if (rs1 == rs2) pc += sext(offset)`

---

### `BNE` <Badge type="info" text="RV32I Base" />

Branch if Not Equal (Desvio se Não Igual)

Verifica se o registrador `rs1` não é igual ao registrador `rs2`, em caso
positivo, modifica o PC para o valor atual somado ao offset com extensão de
sinal.

#### Sintaxe

| Tipo |   31-25   | 24-20 | 19-15 | 14-12 | 11-7 |    6-0     |
| :--: | :-------: | :---: | :---: | :---: | :--: | :--------: |
|  B   | offset[12 | 10:5] |  rs2  |  rs1  | 001  | offset[4:1 |

#### Formato

`bnq rs1, rs2, offset`

#### Implementação

`if (rs1 != rs2) pc += sext(offset)`

---

### `BLT` <Badge type="info" text="RV32I Base" />

Branch if Less Than (Desvio se Menor que)

Verifica se o registrador `rs1` é menor que o registrador `rs2`, considerando
que são números em complemento de dois, em caso positivo, modifica o PC para o
valor atual somado ao offset com extensão de sinal.

#### Sintaxe

| Tipo |   31-25   | 24-20 | 19-15 | 14-12 | 11-7 |    6-0     |
| :--: | :-------: | :---: | :---: | :---: | :--: | :--------: |
|  B   | offset[12 | 10:5] |  rs2  |  rs1  | 000  | offset[4:1 |

#### Formato

`blt rs1, rs2, offset`

#### Implementação

`if (rs1 < rs2) pc += sext(offset)`

---

### `BGE` <Badge type="info" text="RV32I Base" />

Branch if Greater Than or Equal(Desvio se Maior ou Igual que)

Verifica se o registrador `rs1` é maior ou igual ao registrador `rs2`,
considerando que são números em complemento de dois, em caso positivo, modifica
o PC para o valor atual somado ao offset com extensão de sinal.

#### Sintaxe

| Tipo |   31-25   | 24-20 | 19-15 | 14-12 | 11-7 |    6-0     |
| :--: | :-------: | :---: | :---: | :---: | :--: | :--------: |
|  B   | offset[12 | 10:5] |  rs2  |  rs1  | 101  | offset[4:1 |

#### Formato

`bge rs1, rs2, offset`

#### Implementação

`if (rs1 >= rs2) pc += sext(offset)`

---

### `BLTU` <Badge type="info" text="RV32I Base" />

Branch if Less Than Unsigned(Desvio se Menor que Sem Sinal)

Verifica se o registrador `rs1` é menor que o registrador `rs2`, considerando
que são números sem sinal, em caso positivo, modifica o PC para o valor atual
somado ao offset com extensão de sinal.

#### Sintaxe

| Tipo |   31-25   | 24-20 | 19-15 | 14-12 | 11-7 |    6-0     |
| :--: | :-------: | :---: | :---: | :---: | :--: | :--------: |
|  B   | offset[12 | 10:5] |  rs2  |  rs1  | 110  | offset[4:1 |

#### Formato

`bltu rs1, rs2, offset`

#### Implementação

`if (rs1 < rs2) pc += sext(offset)`

---

### `BGEU` <Badge type="info" text="RV32I Base" />

Branch if Greater or Equal Than Unsigned(Desvio se Maior ou Igual que Sem Sinal)

Verifica se o registrador `rs1` é maior ou igual que o registrador `rs2`,
considerando que são números sem sinal, em caso positivo, modifica o PC para o
valor atual somado ao offset com extensão de sinal.

#### Sintaxe

| Tipo |   31-25   | 24-20 | 19-15 | 14-12 | 11-7 |    6-0     |
| :--: | :-------: | :---: | :---: | :---: | :--: | :--------: |
|  B   | offset[12 | 10:5] |  rs2  |  rs1  | 110  | offset[4:1 |

#### Formato

`bgeu rs1, rs2, offset`

#### Implementação

`if (rs1 >= rs2) pc += sext(offset)`

---

## Busca na Memória

### `LB` <Badge type="info" text="RV32I Base" />

Load Byte (Carrega Byte).

Carrega um byte da memória no endereço `rs1 + sext(offset)` e armazena o valor
no registrador `rd`, com extensão de sinal.

#### Sintaxe

| Tipo |    31-20     | 19-15 | 14-12 | 11-7 | 6-0  |
| :--: | :----------: | :---: | :---: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  000  |  rd  | LOAD |

#### Formato

`lb rd, offset(rs1)`

#### Implementação

`x[rd] = sext(M[x[rs1] + sext(offset)][7:0])`

---

### `LH` <Badge type="info" text="RV32I Base" />

Load Halfword (Carrega Halfword).

Carrega dois bytes da memória no endereço `rs1 + sext(offset)` e armazena o
valor no registrador `rd`, com extensão de sinal.

#### Sintaxe

| Tipo |    31-20     | 19-15 | 14-12 | 11-7 | 6-0  |
| :--: | :----------: | :---: | :---: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  001  |  rd  | LOAD |

#### Formato

`lh rd, offset(rs1)`

#### Implementação

`x[rd] = sext(M[x[rs1] + sext(offset)][15:0])`

---

### `LBU` <Badge type="info" text="RV32I Base" />

Load Byte Unsigned(Carrega Byte Sem Sinal).

Carrega um byte da memória no endereço `rs1 + sext(offset)` e armazena o valor
no registrador `rd`, com extensão de zero.

#### Sintaxe

| Tipo |    31-20     | 19-15 | 14-12 | 11-7 | 6-0  |
| :--: | :----------: | :---: | :---: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  100  |  rd  | LOAD |

#### Formato

`lbu rd, offset(rs1)`

#### Implementação

`x[rd] = M[x[rs1] + sext(offset)][7:0]`

---

### `LHU` <Badge type="info" text="RV32I Base" />

Load Halfword Unsigned(Carrega Halfword Sem Sinal).

Carrega dois bytes da memória no endereço `rs1 + sext(offset)` e armazena o
valor no registrador `rd`, com extensão de zero.

#### Sintaxe

| Tipo |    31-20     | 19-15 | 14-12 | 11-7 | 6-0  |
| :--: | :----------: | :---: | :---: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  101  |  rd  | LOAD |

#### Formato

`lhu rd, offset(rs1)`

#### Implementação

`x[rd] = M[x[rs1] + sext(offset)][15:0]`

---

### `LW` <Badge type="info" text="RV32I Base" />

Load Word (Carrega Word).

Carrega quatro bytes da memória no endereço `rs1 + sext(offset)` e armazena o
valor no registrador `rd`.

#### Sintaxe

| Tipo |    31-20     | 19-15 | 14-12 | 11-7 | 6-0  |
| :--: | :----------: | :---: | :---: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  010  |  rd  | LOAD |

#### Formato

`lw rd, offset(rs1)`

#### Implementação

`x[rd] = sext(M[x[rs1] + sext(offset)][31:0])`

---

## Escrita na Memória

### `SB` <Badge type="info" text="RV32I Base" />

Store Byte (Armazena Byte).

Armazena o byte menos significativo do registrador `rs2` na memória no endereço
`rs1 + sext(offset)`.

#### Sintaxe

| Tipo |    31-25     | 24-20 | 19-15 | 14-12 |    11-7     |  6-0  |
| :--: | :----------: | :---: | :---: | :---: | :---------: | :---: |
|  S   | offset[11:5] |  rs2  |  rs1  |  000  | offset[4:0] | STORE |

#### Formato

`sb rs2, offset(rs1)`

#### Implementação

`M[x[rs1] + sext(offset)] = x[rs2][7:0]`

---

### `SH` <Badge type="info" text="RV32I Base" />

Store Halfword (Armazena Halfword).

Armazena os dois bytes menos significativo do registrador `rs2` na memória no
endereço `rs1 + sext(offset)`.

#### Sintaxe

| Tipo |    31-25     | 24-20 | 19-15 | 14-12 |    11-7     |  6-0  |
| :--: | :----------: | :---: | :---: | :---: | :---------: | :---: |
|  S   | offset[11:5] |  rs2  |  rs1  |  001  | offset[4:0] | STORE |

#### Formato

`sh rs2, offset(rs1)`

#### Implementação

`M[x[rs1] + sext(offset)] = x[rs2][15:0]`

---

### `SW` <Badge type="info" text="RV32I Base" />

Store Word (Armazena Word).

Armazena os quatro bytes menos significativo do registrador `rs2` na memória no
endereço `rs1 + sext(offset)`.

#### Sintaxe

| Tipo |    31-25     | 24-20 | 19-15 | 14-12 |    11-7     |  6-0  |
| :--: | :----------: | :---: | :---: | :---: | :---------: | :---: |
|  S   | offset[11:5] |  rs2  |  rs1  |  010  | offset[4:0] | STORE |

#### Formato

`sw rs2, offset(rs1)`

#### Implementação

`M[x[rs1] + sext(offset)] = x[rs2][31:0]`
