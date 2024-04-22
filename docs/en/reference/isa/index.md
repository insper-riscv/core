---
outline: [2, 3]
---

# Instruction Set

## Syntax

Instructions are 32-bit binary vectors, with their syntax being as follows:

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Type</th>
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

With each segment of the instruction being one of the following:

- `opcode`: Determines a type of instruction or a specific instruction;
- `funct3`: Second parameter used to specify a instruction that belongs to a type determined by the opcode;
- `funct7`: Third parameter used to specify a instruction that belongs to a type determined by the opcode, 
but type has too many instructions to be covered by funct3 alone;
- `rs1`: Address of primary register being used in operation;
- `rs2`: Address of secondary register being used in operation;
- `rd`: Address of destination register;
- `imm`: Immediate vector.

Observation: In some cases, it is possible to see that a bit of the instruction represents a range of bits, such as imm[31:20], for example. These are situations where the most significant bits of the immediate value correspond to the most significant bit of the instruction sign extended.

### Opcode

Opcodes are 7-bit segments of the instruction vector. Each type of instruction 
has an opcode or an instruction has an exclusive opcode. For some types of 
instructions, they are encoded with more than one opcode, following the 
following generalization:

|    None    |   value   |
| :--------: | :-------: |
|     OP     | `0110011` |
|   OP-IMM   | `0010011` |
|   STORE    | `0100011` |
|    LOAD    | `0000011` |
|   BRANCH   | `1100011` |
| **Others** | `XXXXX11` |

### Immediate

Immediates are 32-bit binary vectors. Each type of instruction which uses
the immediate may use a different value of immediate, where it has one of the following syntaxes:


<table>
    <thead>
        <tr>
            <th style="text-align: center;\f">Type</th>
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

Where `inst` represents the instruction segment from which the bit or bytes of the immediate came from.

## Build

---

### `LUI` <Badge type="info" text="RV32I Base" />

Load Upper Immediate.

Loads 32-bit constants. `LUI` places the immediate value into 
the upper 20 bits of register `rd`, filling the lower 12 bits with zeros.

Stores 32-bit constants in registers. `LUI` uses the immediate value from the 20 most significant
bits of the instruction into the 20 most significant bits of the destination register `rd`,
filling the 12 least significant bits with zeros.

#### Syntax

| Type |   31-12    |    11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: |
|  U   | imm[31:12] |     rd     | `0110111` |

#### Format

`lui rd, imm`

#### Implementation

`x[rd] = imm[31:12] << 12`

---

### `AUIPC` <Badge type="info" text="RV32I Base" />

Add Upper Immediate.

Shifts the immediate value, which is the 20 most significant bits of the instruction, 
12 bits to the left, filling the 12 least significant bits with zeros 
and adds it to the PC. Writes the result into register `rd`.

#### Syntax

| Type |   31-12    |    11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: |
|  U   | imm[31:12] |    rd      | `0010111` |

#### Format

`auipc rd, imm`

#### Implementation

`x[rd] = pc + sext(immediate[31:12] << 12)`

---

## Arithmetic

### `ADD` <Badge type="info" text="RV32I Base" />

Add.

Adds registers `rs1` and `rs2` and stores the result into register `rd`. 
If overflow occurs, it is ignored.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000000  |    rs2     |    rs1    |   000    |    rd     | `0110011` |    

#### Format

`add rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] + x[rs2]`

---

### `ADDI` <Badge type="info" text="RV32I Base" />

Add Immediate.

Adds register `rs1` with the sign-extended immediate and stores the result into register `rd`.
If overflow occurs, it is ignored.

#### Syntax
  
| Tipo |         31-20       |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :-----------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   immediate[11:0]   |    rs1    |   000    |    rd     | `0010011` |  

#### Format

`addi rd, rs1, immediate`

#### Implementation

`x[rd] = x[rs1] + sext(immediate)`

---

### `SUB` <Badge type="info" text="RV32I Base" />

Subtract.

Subtracts register `rs2` from `rs1` and stores the result into register `rd`. 
If overflow occurs, it is ignored.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0100000  |    rs2     |    rs1    |   000    |    rd     | `0110011` |    

#### Format

`sub rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] - x[rs2]`

---

### `MUL` <Badge type="tip" text="“M” Standard Extension" />

Multiply.

Multiplies registers `rs1` and `rs2` and stores the result into register `rd`. 
If overflow occurs, it is ignored.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000001  |    rs2     |    rs1    |   000    |    rd     | `0110011` |    

#### Format

`mul rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] × x[rs2]`

---

### `MULH` <Badge type="tip" text="“M” Standard Extension" />

Multiply High.

Multiplies registers `rs1` and `rs2`, treating them as two's complement numbers,
and stores the upper half of the product into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000001  |    rs2     |    rs1    |   001    |    rd     | `0110011` |    

#### Format

`mulh rd, rs1, rs2`

#### Implementation

`x[rd] = (x[rs1] × x[rs2]) >> XLEN`

---

### `MULHSU` <Badge type="tip" text="“M” Standard Extension" />

Multiply High Signed and Unsigned.

Multiplies registers `rs1` and `rs2`, treating `rs1` as a two's complement number
and `rs2` as an unsigned number, and stores the upper half of the product into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000001  |    rs2     |    rs1    |   010    |    rd     | `0110011` |   

#### Format

`mulhsu rd, rs1, rs2`

#### Implementation

`x[rd] = (x[rs1] * x[rs2]) >> XLEN`

---

### `MULHU` <Badge type="tip" text="“M” Standard Extension" />

Multiply High Unsigned.

Multiplies registers `rs1` and `rs2`, treating both as unsigned numbers, and stores
the upper half of the product into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000001  |    rs2     |    rs1    |   011    |    rd     | `0110011` |   

#### Format

`mulhu rd, rs1, rs2`

#### Implementation

`x[rd] = (x[rs1] × x[rs2]) >> XLEN`

---

### `DIV` <Badge type="tip" text="“M” Standard Extension" />

Divide.

Divides register `rs1` by `rs2`, treating them as two's complement numbers, rounding
towards zero, and stores the quotient into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000001  |    rs2     |    rs1    |   100    |    rd     | `0110011` |    

#### Format

`div rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] ÷ x[rs2]`

---

### `DIVU` <Badge type="tip" text="“M” Standard Extension" />

Divide Unsigned.

Divides register `rs1` by `rs2`, treating them as unsigned numbers, rounding
towards zero, and stores the quotient into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000001  |    rs2     |    rs1    |   101    |    rd     | `0110011` |    

#### Format

`div rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] ÷ x[rs2]`

---

### `REM` <Badge type="tip" text="“M” Standard Extension" />

Remainder.

Divides register `rs1` by `rs2`, treating them as two's complement numbers, rounding
towards zero, and stores the remainder into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000001  |    rs2     |    rs1    |   110    |    rd     | `0110011` |    

#### Format

`rem rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] % x[rs2]`

---

### `REMU` <Badge type="tip" text="“M” Standard Extension" />

Remainder Unsigned.

Divides register `rs1` by `rs2`, treating them as unsigned numbers, rounding
towards zero, and stores the remainder into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000001  |    rs2     |    rs1    |   111    |    rd     | `0110011` |    

#### Format

`rem rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] % x[rs2]`

---

## Logical

### `XOR` <Badge type="info" text="RV32I Base" />

Exclusive OR.

Performs the logical XOR operation, bit-wise, between registers `rs1` and `rs2`, 
and stores the result into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000000  |    rs2     |    rs1    |   100    |    rd     | `0110011` |    

#### Format

`xor rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] ˆ x[rs2]`

---

### `XORI` <Badge type="info" text="RV32I Base" />

Exclusive OR Immediate.

Performs the logical XOR operation, bit-wise, between register `rs1` and the 
sign-extended immediate, and stores the result into register `rd`.

#### Syntax
  
| Tipo |         31-20       |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :-----------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   immediate[11:0]   |    rs1    |   100    |    rd     | `0010011` |  

#### Format

`xori rd, rs1, immediate`

#### Implementation

`x[rd] = x[rs1] ˆ sext(immediate)`

---

### `OR` <Badge type="info" text="RV32I Base" />

OR.

Performs the logical OR operation, bit-wise, between registers `rs1` and `rs2`, 
and stores the result into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000000  |    rs2     |    rs1    |   110    |    rd     | `0110011` |    

#### Format

`or rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] | x[rs2]`

---

### `ORI` <Badge type="info" text="RV32I Base" />

OR Immediate.

Performs the logical OR operation, bit-wise, between register `rs1` and the sign-extended immediate,
and stores the result into register `rd`.

#### Syntax
  
| Tipo |         31-20       |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :-----------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   immediate[11:0]   |    rs1    |   110    |    rd     | `0010011` |  

#### Format

`ori rd, rs1, immediate`

#### Implementation

`x[rd] = x[rs1] | sext(immediate)`

---

### `AND` <Badge type="info" text="RV32I Base" />

AND.

Performs the logical AND operation, bit-wise, between registers `rs1` and `rs2`, 
and stores the result into register `rd`.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000000  |    rs2     |    rs1    |   111    |    rd     | `0110011` |    

#### Format

`and rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] & x[rs2]`

---

### `ANDI` <Badge type="info" text="RV32I Base" />

AND Immediate (E Imediato).

Performs the logical AND operation, bit-wise, between register `rs1` and the sign-extended immediate,
and stores the result into register `rd`.

#### Syntax
  
| Tipo |         31-20       |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :-----------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   immediate[11:0]   |    rs1    |   111    |    rd     | `0010011` |  

#### Format

`andi rd, rs1, immediate`

#### Implementation

`x[rd] = x[rs1] & sext(immediate)`


---

## Shift

### `SLL` <Badge type="info" text="RV32I Base" />

Shift Left Logical.

Shifts the value of register `rs1` to the left by the number of positions indicated by the
5 least significant bits of the value of register `rs2`. The remaining bits
of `rs2` are ignored. Empty bits in `rs1` are filled with zeros. The result
is written into register `rd`.

#### Syntax

| Type |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000000  |     rs2    |  rs1      |   001    |    rd     | `0110011` |    

#### Format

`sll rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] << x[rs2]`


---

### `SLLI` <Badge type="info" text="RV32I Base" />

Shift Left Logical Immediate.

Shifts the value of register `rs1` to the left by the number of positions indicated by `shamt`.
Empty bits in `rs1` are filled with zeros. The result is written into register `rd`.
Only permitted when `shamt[5] = 0`.

#### Syntax

| Type |   31-26    |   25-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  I   |   000000   |   shamt    |    rs1    |   001    |    rd     | `0010011` |    

#### Format

`slli rd, rs1, shamt`

#### Implementation

`x[rd] = x[rs1] << shamt`


---

### `SRL` <Badge type="info" text="RV32I Base" />

Shift Right Logical.

Shifts the value of register `rs1` to the right by the number of positions indicated by the
5 least significant bits of the value of register `rs2`. The remaining bits
of `rs2` are ignored. Empty bits in `rs1` are filled with zeros. The result
is written into register `rd`.


#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000000  |    rs2     |    rs1    |   101    |    rd     | `0110011` |    

#### Format

`srl rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] >> x[rs2]`

---

### `SRLI` <Badge type="info" text="RV32I Base" />

Shift Right Logical Immediate.

Shifts the value of register `rs1` to the right by the number of positions indicated by `shamt`.
Empty bits in `rs1` are filled with zeros. The result is written into register `rd`.
Only permitted when `shamt[5] = 0`.


#### Syntax

| Tipo |   31-26    |   25-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  I   |   000000   |   shamt    |    rs1    |   101    |    rd     | `0010011` |    

#### Format

`srli rd, rs1, shamt`

#### Implementation

`x[rd] = x[rs1] >>shamt`

---

### `SRA` <Badge type="info" text="RV32I Base" />

Shift Right Arithmetic.

Shifts the value of register `rs1` to the right by the number of positions indicated by the
5 least significant bits of the value of register `rs2`. The remaining bits
of `rs2` are ignored. Empty bits in `rs1` are filled with copies of the most significant bit
of `rs1`. The result is written into register `rd`.


#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0100000  |    rs2     |    rs1    |   101    |    rd     | `0110011` |    

#### Format

`sra rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] >> x[rs2]`

---

### `SRAI` <Badge type="info" text="RV32I Base" />

Shift Right Arithmetic Immediate.

Shifts the value of register `rs1` to the right by the number of positions indicated by `shamt`.
Empty bits in `rs1` are filled with copies of the most significant bit of `rs1`.
The result is written into register `rd`.
Only permitted when `shamt[5] = 0`.


#### Syntax

| Tipo |   31-26    |   25-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  I   |   010000   |   shamt    |    rs1    |   101    |    rd     | `0010011` |    

#### Format

`srai rd, rs1, shamt`

#### Implementation

`x[rd] = x[rs1] >> shamt`

---

## Compare

### `SLT` <Badge type="info" text="RV32I Base" />

Set if Less Than.

Checks if register `rs1` is less than register `rs2`, treating them as two's complement numbers.
If true, stores 1 into register `rd`, otherwise stores 0.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000000  |    rs2     |    rs1    |   010    |    rd     | `0110011` |    

#### Format

`slt rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] < x[rs2]`

---

### `SLTI` <Badge type="info" text="RV32I Base" />

Set if Less Than Immediate.

Checks if register `rs1` is less than the sign-extended immediate, treating them as two's complement numbers.
If true, stores 1 into register `rd`, otherwise stores 0.

#### Syntax
  
| Tipo |         31-20       |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :-----------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   immediate[11:0]   |    rs1    |   010    |    rd     | `0010011` |  

#### Format

`slti rd, rs1, immediate`

#### Implementation

`x[rd] = x[rs1] < sext(immediate)`

---

### `SLTIU` <Badge type="info" text="RV32I Base" />

Set if Less Than Immediate Unsigned.

Checks if register `rs1` is less than the sign-extended immediate, treating them as unsigned numbers.
If true, stores 1 into register `rd`, otherwise stores 0.

#### Syntax
  
| Tipo |         31-20       |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :-----------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   immediate[11:0]   |    rs1    |   011    |    rd     | `0010011` |  

#### Format

`slti rd, rs1, immediate`

#### Implementation

`x[rd] = x[rs1] < sext(immediate)`

---

### `SLTU` <Badge type="info" text="RV32I Base" />

Set if Less Than Unsigned.

Checks if register `rs1` is less than register `rs2`, treating them as unsigned numbers.
If true, stores 1 into register `rd`, otherwise stores 0.

#### Syntax

| Tipo |   31-25    |   24-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------: | :--------: | :-------: | :------: | :-------: | :-------: |
|  R   |   0000000  |    rs2     |    rs1    |   011    |    rd     | `0110011` |    

#### Format

`sltu rd, rs1, rs2`

#### Implementation

`x[rd] = x[rs1] < x[rs2]`


---

## Link

### `JAL` <Badge type="info" text="RV32I Base" />

Jump and Link.

Writes the address of the next instruction (PC+4) into register `rd` and modifies the PC to the current
value plus the sign-extended offset. If `rd` is omitted, the return address is stored in `x1`.

#### Syntax

| Tipo |             31-12           |    11-7   |    6-0    |
| :--: | :-------------------------: | :-------: | :-------: |
|  J   |  offset[20|10:1|11|19:12]   |    rd     | `1100011` |

#### Format

`jal rd, offset`

#### Implementation

`x[rd] = pc+4; pc += sext(offset)`

---

### `JALR` <Badge type="info" text="RV32I Base" />

Jump and Link Register.

Copies the PC to `rs1 + sext(offset)`, masks the least significant bit of the resulting address, and
stores the previous PC+4 address into register `rd`. If `rd` is omitted, the value is stored in `x1`.

#### Syntax
  
| Tipo |         31-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   offset[11:0]   |    rs1    |   000    |    rd     | `1100111` |  

#### Format

`jalr rd, offset(rs1) `

#### Implementation

`t =pc+4; pc=(x[rs1]+sext(offset))&∼1; x[rd]=t`

---

## Branch

### `BEQ` <Badge type="info" text="RV32I Base" />

Branch if Equal.

Checks if register `rs1` is equal to register `rs2`. If true, modifies the PC
to the current value plus the sign-extended offset.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  B   |   offset[12|10:5]  |    rs2     |    rs1    |   000    |    offset[4:1|11]     | `1100011` |    

#### Format

`beq rs1, rs2, offset`

#### Implementation

`if (rs1 == rs2) pc += sext(offset)`

---

### `BNE` <Badge type="info" text="RV32I Base" />

Branch if Not Equal.

Checks if register `rs1` is different to register `rs2`. If true, modifies the PC
to the current value plus the sign-extended offset.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  B   |   offset[12|10:5]  |    rs2     |    rs1    |   001    |    offset[4:1|11]     | `1100011` |    

#### Format

`bnq rs1, rs2, offset`

#### Implementation

`if (rs1 != rs2) pc += sext(offset)`

---

### `BLT` <Badge type="info" text="RV32I Base" />

Branch if Less Than.

Checks if register `rs1` is less than register `rs2`, treating them as two's complement numbers. 
If true, modifies the PC to the current value plus the sign-extended offset.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  B   |   offset[12|10:5]  |    rs2     |    rs1    |   000    |    offset[4:1|11]     | `1100011` |    

#### Format

`blt rs1, rs2, offset`

#### Implementation

`if (rs1 < rs2) pc += sext(offset)`

---

### `BGE` <Badge type="info" text="RV32I Base" />

Branch if Greater Than or Equal to.

Checks if register `rs1` is greater than or equal to register `rs2`, treating them as two's complement numbers. 
If true, modifies the PC to the current value plus the sign-extended offset.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  B   |   offset[12|10:5]  |    rs2     |    rs1    |   101    |    offset[4:1|11]     | `1100011` |    

#### Format

`bge rs1, rs2, offset`

#### Implementation

`if (rs1 >= rs2) pc += sext(offset)`

---

### `BLTU` <Badge type="info" text="RV32I Base" />

Branch if Less Than Unsigned.

Checks if register `rs1` is less than register `rs2`, treating them as unsigned numbers. 
If true, modifies the PC to the current value plus the sign-extended offset.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  B   |   offset[12|10:5]  |    rs2     |    rs1    |   110    |    offset[4:1|11]     | `1100011` |    

#### Format

`bltu rs1, rs2, offset`

#### Implementation

`if (rs1 < rs2) pc += sext(offset)`

---

### `BGEU` <Badge type="info" text="RV32I Base" />

Branch if Greater Than or Equal To Unsigned.

Checks if register `rs1` is greater than or equal to register `rs2`, treating them as unsigned numbers. 
If true, modifies the PC to the current value plus the sign-extended offset.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  B   |   offset[12|10:5]  |    rs2     |    rs1    |   110    |    offset[4:1|11]     | `1100011` |    

#### Format

`bgeu rs1, rs2, offset`

#### Implementation

`if (rs1 >= rs2) pc += sext(offset)`

---

## Loads

### `LB` <Badge type="info" text="RV32I Base" />

Load Byte.

Loads a byte from memory at address `rs1 + sext(offset)` and stores the value into register `rd`,
with sign extension.

#### Syntax
  
| Tipo |         31-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   offset[11:0]   |    rs1    |   000    |    rd     | `0000011` |  

#### Format

`lb rd, offset(rs1)`

#### Implementation

`x[rd] = sext(M[x[rs1] + sext(offset)][7:0])`

---

### `LH` <Badge type="info" text="RV32I Base" />

Load Halfword.

Loads two bytes from memory at address `rs1 + sext(offset)` and stores the value into register `rd`,
with sign extension.

#### Syntax
  
| Tipo |         31-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   offset[11:0]   |    rs1    |   001    |    rd     | `0000011` |  

#### Format

`lh rd, offset(rs1)`

#### Implementation

`x[rd] = sext(M[x[rs1] + sext(offset)][15:0])`


---

### `LBU` <Badge type="info" text="RV32I Base" />

Load Byte Unsigned.

Loads a byte from memory at address `rs1 + sext(offset)` and stores the value into register `rd`,
with zero extension.

#### Syntax
  
| Tipo |         31-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   offset[11:0]   |    rs1    |   100    |    rd     | `0000011` |  

#### Format

`lbu rd, offset(rs1)`

#### Implementation

`x[rd] = M[x[rs1] + sext(offset)][7:0]`

---

### `LHU` <Badge type="info" text="RV32I Base" />

Load Halfword Unsigned.

Loads two bytes from memory at address `rs1 + sext(offset)` and stores the value into register `rd`,
with zero extension.

#### Syntax
  
| Tipo |         31-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   offset[11:0]   |    rs1    |   101    |    rd     | `0000011` |  

#### Format

`lhu rd, offset(rs1)`

#### Implementation

`x[rd] = M[x[rs1] + sext(offset)][15:0]`

---

### `LW` <Badge type="info" text="RV32I Base" />

Load Word.

Loads four bytes from memory at address `rs1 + sext(offset)` and stores the value into register `rd`.

#### Syntax
  
| Tipo |         31-20    |   19-15   |  14-12   |   11-7    |    6-0    |
| :--: | :--------------: | :-------: | :------: | :-------: | :-------: |
|  I   |   offset[11:0]   |    rs1    |   010    |    rd     | `0000011` |  

#### Format

`lw rd, offset(rs1)`

#### Implementation

`x[rd] = sext(M[x[rs1] + sext(offset)][31:0])`

---

## Stores

### `SB` <Badge type="info" text="RV32I Base" />

Store Byte.

Stores the least significant byte of register `rs2` into memory at address `rs1 + sext(offset)`.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  S   |    offset[11:5]    |    rs2     |    rs1    |   000    |       offset[4:0]     | `0100011` |    

#### Format

`sb rs2, offset(rs1)`

#### Implementation

`M[x[rs1] + sext(offset)] = x[rs2][7:0]`

---

### `SH` <Badge type="info" text="RV32I Base" />

Store Halfword.

Stores the two least significant bytes of register `rs2` into memory at address `rs1 + sext(offset)`.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  S   |    offset[11:5]    |    rs2     |    rs1    |   001    |       offset[4:0]     | `0100011` |    

#### Format

`sh rs2, offset(rs1)`

#### Implementation

`M[x[rs1] + sext(offset)] = x[rs2][15:0]`

---

### `SW` <Badge type="info" text="RV32I Base" />

Store Word.

Stores the four least significant bytes of register `rs2` into memory at address `rs1 + sext(offset)`.

#### Syntax

| Tipo |        31-25       |   24-20    |   19-15   |  14-12   |          11-7         |    6-0    |
| :--: | :----------------: | :--------: | :-------: | :------: | :-------------------: | :-------: |
|  S   |    offset[11:5]    |    rs2     |    rs1    |   010    |       offset[4:0]     | `0100011` |    

#### Format

`sw rs2, offset(rs1)`

#### Implementation

`M[x[rs1] + sext(offset)] = x[rs2][31:0]`
