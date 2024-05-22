---
outline: [2, 3]
---

## Conjunto de Instruções

### Sintaxe

As instruções são vetores binários de 32 _bits_, podendo ser classificadas de duas formas: segundo sua sintaxe,
ou de acordo com sua função. No que se refere à sintaxe, as instruções podem ser do tipo R, I, S, B, U ou J, como demonstrado na Tabela Sintaxe.

![alt text](/images/reference/report_components/tabela_sintaxe.drawio.svg)
<p class="table_subtitle"><b>Tabela Sintaxe</b> - Tabela de Sintaxe dos tipos de instrução.</p>

Instruções do tipo R são usadas para realizar operações entre registradores.

Instruções do tipo I são utilizadas para realizar operações em registradores com uso de valores imediatos.

Instruções do tipo S armazenam valores na memória.

Instruções do tipo B realizam desvios no programa dependendo do resultado da comparação de valores em dois registradores.

Instruções do tipo U são empregadas em operações que usam os 20 _bits_ mais significativos da instrução como imediato, com os _bits_ remanescentes sendo 0.

Apenas a instrução JAL (_Jump and Link_ - Salto e Conexão) é do tipo J.

Sendo, para cada segmento da instrução:

- `opcode`: Codifica o tipo de instrução ou uma instrução específica;
- `funct3`: Codifica a operacionalização da instrução;
- `funct7`: Codifica uma variação da operacionalização;
- `rs1`: Endereça registrador de recurso primário;
- `rs2`: Endereça registrador de recurso secundário;
- `rd`: Endereça registrador de destinação;
- `imm`: Vetor do imediato.

Observação: Em alguns caso, é possível ver que um_bit_ da instrução representa um 
intervalo de _bits_, como imm[31:20] por exemplo. Esses são casos onde os _bits_ 
mais significativos do imediato são o_bit_ mais significativo da instrução extendido.

#### Opcode

Opcodes são segmentos de 7 _bits_ do vetor de instrução. Cada tipo de instrução
possui um opcode ou uma instrução possui um opcode exclusivo. Para alguns tipos
de instrução, são codificados com mais de um opcode, estando estes exemplificados
na Tabela Opcode.

|    None    |   valor   |
| :--------: | :-------: |
|     OP     | `0110011` |
|   OP-IMM   | `0010011` |
|   STORE    | `0100011` |
|    LOAD    | `0000011` |
|   BRANCH   | `1100011` |
| **Outros** | `XXXXX11` |
<p class="table_subtitle"><b>Tabela Opcode</b> - Tabela com exemplos de opcodes comuns.</p>

#### Imediato

Os imediatos são vetores binários de 32 _bits_. Cada tipo de instrução com
imediato possui uma sintaxe de imediato demonstrada na Tabela Imediato.

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
<p class="table_subtitle"><b>Tabela Imediato</b> - Tabela com a sintaxe dos imediatos de acordo com seu tipo de instrução.</p>

Sendo, para cada segmento, `inst` o vetor da instrução.

---

Por sua vez, a classificação das instruções segundo sua funcionalidade divide-as em grupos independentemente de sua estrutura. Esses grupos incluem:

- As instruções de construção, que criam valores em registradores;
- As instruções de deslocamento, que realizam operações de deslocamento de _bits_ nos valores armazenados nos registradores;
- As instruções aritméticas, que efetuam operações matemáticas;
- As instruções lógicas, que são responsáveis por operações lógicas;
- As instruções de desvio, que alteram o fluxo de execução do programa com base em condições; 
- As instruções de salto, que permitem saltos para outras partes do programa; 
- As instruções de carregar, que carregam valores da memória para os registradores; 
- As instruções de armazenar, que guardam valores dos registradores na memória.

Nas instruções que se seguem, RV32I Base significa que elas pertencem ao conjunto base de instruções para inteiros de 32 _bits_, e “M” _Standard Extension_ significa que elas pertencem à extensão de Multiplicação:

### Carrega Constante

#### `LUI` <Badge type="info" text="RV32I Base" />

_Load Upper Immediate_ (Carregar Superior Imediato).

Carrega registradores com valores constantes de 32 _bits_. `LUI` guarda o valor 
imediato dos 20 _bits_ mais significativos da instrução nos 20 _bits_ mais 
significativos do registrador de destino `rd`, preenchendo os 12 _bits_ menos 
significativos com zero.

##### Sintaxe

A instrução LUI é do tipo U, tendo um opcode próprio, como ilustrado na Tabela LUI.

| Tipo |   31-12    | 11-7 |    6-0    |
| :--: | :--------: | :--: | :-------: |
|  U   | imm[31:12] |  rd  | `0110111` |
<p class="table_subtitle"><b>Tabela LUI</b> - Tabela com sintaxe da instrução LUI.</p>

##### Formato

`lui rd, imm`

##### Implementação

`x[rd] = imm[31:12] << 12`

---

#### `AUIPC` <Badge type="info" text="RV32I Base" />

Add Upper Immediate (Adiciona Superior Imediato).

Desloca o valor do imediato da instrução, que consiste nos 20 _bits_ mais significativos, 
12 _bits_ à esquerda, preenchendo os 12 _bits_ menos significativos com zero, e o adiciona 
ao PC. O resultado é então escrito no registrador de destino `rd`. 

##### Sintaxe

A instrução AUIPC é do tipo U, tendo um opcode próprio, como ilustrado na Tabela AUIPC.

| Tipo |   31-12    | 11-7 |    6-0    |
| :--: | :--------: | :--: | :-------: |
|  U   | imm[31:12] |  rd  | `0010111` |
<p class="table_subtitle"><b>Tabela AUIPC</b> - Tabela com sintaxe da instrução AUIPC.</p>

##### Formato

`auipc rd, imm`

##### Implementação

`x[rd] = pc + sext(imm[31:12] << 12)`

---

### Lógica Aritmética

#### `ADD` <Badge type="info" text="RV32I Base" />

Add (Adição).

Soma o valor armazenado no registrador `rs1` com o valor 
armazenado no registrador `rs2` e armazena o resultado 
no registrador de destino `rd`. Em caso de overflow, ele é ignorado.

##### Sintaxe

A instrução ADD é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela ADD.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000000` |  rs2  |  rs1  |  `000`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela ADD</b> - Tabela com sintaxe da instrução ADD.</p>

##### Formato

`add rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] + x[rs2]`

---

#### `ADDI` <Badge type="info" text="RV32I Base" />

Add Immediate (Adição Imediata).

Soma o valor armazenado no registrador `rs1` com o sinal estendido 
do imediato e armazena o resultado no registrador de destino `rd`. 
Em caso de overflow, ele é ignorado.

##### Sintaxe

A instrução ADDI é do tipo I, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela ADDI.

| Tipo |   31-20   | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :-----: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  `000`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela ADDI</b> - Tabela com sintaxe da instrução ADDI.</p>

##### Formato

`addi rd, rs1, immediate`

##### Implementação

`x[rd] = x[rs1] + sext(immediate)`

---

#### `SUB` <Badge type="info" text="RV32I Base" />

Subtract (Subtração).

Subtrai o valor armazenado no registrador `rs2` do valor 
armazenado no registrador `rs1` e armazena o resultado no 
registrador de destino `rd`. Em caso de overflow, ele é ignorado.

##### Sintaxe

A instrução SUB é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SUB.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0100000` |  rs2  |  rs1  |  `000`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela SUB</b> - Tabela com sintaxe da instrução SUB.</p>

##### Formato

`sub rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] - x[rs2]`

---

#### `MUL` <Badge type="tip" text="“M” Standard Extension" />

Multiply (Multiplicação).

Multiplica o valor armazenado no registrador `rs1` pelo valor 
armazenado no registrador `rs2` e armazena o resultado no 
registrador de destino `rd`. Em caso de overflow, ele é ignorado.

##### Sintaxe

A instrução MUL é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela MUL.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000001` |  rs2  |  rs1  |  `000`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela MUL</b> - Tabela com sintaxe da instrução MUL.</p>

##### Formato

`mul rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] × x[rs2]`

---

#### `MULH` <Badge type="tip" text="“M” Standard Extension" />

Multiply High (Multiplicação Superior).

Multiplica o valor armazenado no registrador `rs1` pelo valor 
armazenado no registrador `rs2` considerando que são números 
de complemento de dois e armazena a metade superior do produto no registrador de destino `rd`.

##### Sintaxe

A instrução MULH é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela MULH.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000001` |  rs2  |  rs1  |  `001`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela MULH</b> - Tabela com sintaxe da instrução MULH.</p>

##### Formato

`mulh rd, rs1, rs2`

##### Implementação

`x[rd] = (x[rs1] × x[rs2]) >> XLEN`

---

#### `MULHSU` <Badge type="tip" text="“M” Standard Extension" />

Multiply High Signed and Unsigned (Multiplicação Superior com Sinal e Sem
Sinal).

Multiplica o valor armazenado no registrador `rs1` pelo valor 
armazenado no registrador `rs2`, considerando que o valor em rs1 é
de complemento de dois e que o valor em rs2 é um número sem sinal, armazenando a metade superior do 
produto no registrador de destino `rd`.

##### Sintaxe

A instrução MULHSU é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela MULHSU.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000001` |  rs2  |  rs1  |  `010`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela MULHSU</b> - Tabela com sintaxe da instrução MULHSU.</p>

##### Formato

`mulhsu rd, rs1, rs2`

##### Implementação

`x[rd] = (x[rs1] * x[rs2]) >> XLEN`

---

#### `MULHU` <Badge type="tip" text="“M” Standard Extension" />

Multiply High Unsigned (Multiplicação Superior Sem Sinal).

Multiplica o valor armazenado no registrador `rs1` pelo valor 
armazenado no registrador `rs2`, considerando que ambos 
são números sem sinal, e armazena a metade superior do produto no registrador de destino `rd`.

##### Sintaxe

A instrução MULHU é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela MULHU.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000001` |  rs2  |  rs1  |  `011`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela MULHU</b> - Tabela com sintaxe da instrução MULHU.</p>

##### Formato

`mulhu rd, rs1, rs2`

##### Implementação

`x[rd] = (x[rs1] × x[rs2]) >> XLEN`

---

#### `DIV` <Badge type="tip" text="“M” Standard Extension" />

Divide (Divisão).

Divide o valor armazenado no registrador `rs1` pelo 
valor armazenado no registrador `rs2`, considerando 
que ambos são números de complemento de dois, arredondando para zero, e 
armazena o quociente no registrador de destino `rd`.


##### Sintaxe

A instrução DIV é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela DIV.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000001` |  rs2  |  rs1  |  `100`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela DIV</b> - Tabela com sintaxe da instrução DIV.</p>

##### Formato

`div rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] ÷ x[rs2]`

---

#### `DIVU` <Badge type="tip" text="“M” Standard Extension" />

Divide Unsigned (Divisão Sem Sinal).

Divide o valor armazenado no registrador `rs1` 
pelo valor armazenado no registrador `rs2`, 
considerando que são números sem sinal, arredondando para zero, e 
armazena o quociente no registrador de destino `rd`.

##### Sintaxe

A instrução DIVU é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela DIVU.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000001` |  rs2  |  rs1  |  `101`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela DIVU</b> - Tabela com sintaxe da instrução DIVU.</p>

##### Formato

`div rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] ÷ x[rs2]`

---

#### `REM` <Badge type="tip" text="“M” Standard Extension" />

Remainder (Resto).

Divide o valor armazenado no registrador `rs1` 
pelo valor armazenado no registrador `rs2`, 
considerando que são números de complemento de dois, arredondando para zero, 
e armazena o resto no registrador de destino `rd`. 

##### Sintaxe

A instrução REM é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela REM.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000001` |  rs2  |  rs1  |  `110`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela REM</b> - Tabela com sintaxe da instrução REM.</p>

##### Formato

`rem rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] % x[rs2]`

---

#### `REMU` <Badge type="tip" text="“M” Standard Extension" />

Remainder Unsigned (Resto Sem Sinal).

Divide o valor armazenado no registrador `rs1` pelo valor 
armazenado no registrador `rs2`, considerando que são 
números sem sinal, arredondando para zero, e armazena o resto no registrador de destino `rd`. 

##### Sintaxe

A instrução REMU é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela REMU.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000001` |  rs2  |  rs1  |  `111`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela REMU</b> - Tabela com sintaxe da instrução REMU.</p>

##### Formato

`rem rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] % x[rs2]`

---

### Lógicas Booleana

#### `XOR` <Badge type="info" text="RV32I Base" />

Exclusive OR (OU Exclusivo).

Realiza a operação lógica XOR,_bit_ a_bit_, entre os valores armazenados nos 
registradores `rs1` e `rs2` e armazena o resultado no registrador de destino `rd`.

##### Sintaxe

A instrução XOR é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela XOR.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000000` |  rs2  |  rs1  |  `100`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela XOR</b> - Tabela com sintaxe da instrução XOR.</p>

##### Formato

`xor rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] ˆ x[rs2]`

---

#### `XORI` <Badge type="info" text="RV32I Base" />

Exclusive OR Immediate (OU Exclusivo Imediato).

Realiza a operação lógica XOR,_bit_ a_bit_, entre o valor armazenado no registrador `rs1` e o imediato
com sinal estendido e armazena o resultado no registrador de destino `rd`.

##### Sintaxe

A instrução XORI é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela XORI.

| Tipo |   31-20   | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :-----: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  `100`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela XORI</b> - Tabela com sintaxe da instrução XORI.</p>

##### Formato

`xori rd, rs1, immediate`

##### Implementação

`x[rd] = x[rs1] ˆ sext(immediate)`

---

#### `OR` <Badge type="info" text="RV32I Base" />

OR (OU).

Realiza a operação lógica OR,_bit_ a_bit_, entre os valores armazenados nos registradores `rs1` e `rs2` e
armazena o resultado no registrador de destino `rd`.

##### Sintaxe

A instrução OR é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela OR.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000000` |  rs2  |  rs1  |  `110`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela OR</b> - Tabela com sintaxe da instrução OR.</p>

##### Formato

`or rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] | x[rs2]`

---

#### `ORI` <Badge type="info" text="RV32I Base" />

OR Immediate (OU Imediato).

Realiza a operação lógica OR,_bit_ a_bit_, entre o valor armazenado no registrador `rs1` e o imediato
com sinal estendido e armazena o resultado no registrador de destino `rd`.

##### Sintaxe

A instrução ORI é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela ORI.

| Tipo |   31-20   | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :-----: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  `110`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela ORI</b> - Tabela com sintaxe da instrução ORI.</p>

##### Formato

`ori rd, rs1, immediate`

##### Implementação

`x[rd] = x[rs1] | sext(immediate)`

---

#### `AND` <Badge type="info" text="RV32I Base" />

AND (E).

Realiza a operação lógica AND,_bit_ a_bit_, entre os valores armazenados nos registradores `rs1` e `rs2` e
armazena o resultado no registrador de destino `rd`.

##### Sintaxe

A instrução AND é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela AND.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000000` |  rs2  |  rs1  |  `111`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela AND</b> - Tabela com sintaxe da instrução AND.</p>

##### Formato

`and rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] & x[rs2]`

---

#### `ANDI` <Badge type="info" text="RV32I Base" />

AND Immediate (E Imediato).

Realiza a operação lógica OR,_bit_ a_bit_, entre o valor armazenado no registrador `rs1` e o imediato
com sinal estendido e armazena o resultado no registrador de destino `rd`.

##### Sintaxe

A instrução ANDI é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela ANDI.

| Tipo |   31-20   | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :-----: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  `111`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela ANDI</b> - Tabela com sintaxe da instrução ANDI.</p>

##### Formato

`andi rd, rs1, immediate`

##### Implementação

`x[rd] = x[rs1] & sext(immediate)`

---

### Operação de Deslocamento

#### `SLL` <Badge type="info" text="RV32I Base" />

Shift Left Logical (Deslocamento à Esquerda Lógico).

Desloca o valor armazenado no registrador `rs1` à esquerda pelo número de posições indicado
pelos 5 _bits_ menos significativos do valor armazenado no registrador `rs2`. Os _bits_
remanescentes de `rs2` são ignorados. Os _bits_ vazios de `rs1` são preenchidos
com zeros. O resultado é escrito no registrador de destino `rd`.

##### Sintaxe

A instrução SLL é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SLL.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000000` |  rs2  |  rs1  |  `001`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela SLL</b> - Tabela com sintaxe da instrução SLL.</p>

##### Formato

`sll rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] << x[rs2]`

---

#### `SLLI` <Badge type="info" text="RV32I Base" />

Shift Left Logical Immediate (Deslocamento à Esquerda Lógico Imediato).

Desloca o valor armazenado no registrador `rs1` à esquerda pelo número de posições indicado
pelo `shamt`. Os _bits_ vazios de `rs1` são preenchidos com zeros. O resultado é
escrito no registrador de destino `rd`. Caso se decida atualizar o processador para uma
arquitetura de 64 bits, esta instrução terá sua sintaxe alterada (o shamt e o funct7 passam
a ter 6 bits cada).

##### Sintaxe

A instrução SLLI é do tipo I, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SLLI.

| Tipo |   31-26   | 24-20 | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :----: |
|  I   | `0000000` | shamt |  rs1  |  `001`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela SLLI</b> - Tabela com sintaxe da instrução SLLI.</p>

##### Formato

`slli rd, rs1, shamt`

##### Implementação

`x[rd] = x[rs1] << shamt`

---

#### `SRL` <Badge type="info" text="RV32I Base" />

Shift Right Logical (Deslocamento à Direita Lógico).

Desloca o valor armazenado no registrador `rs1` à direita pelo número de posições indicado
pelos 5 _bits_ menos significativos do valor armazenado no registrador `rs2`. Os _bits_
remanescentes de `rs2` são ignorados. Os _bits_ vazios de `rs1` são preenchidos
com zeros. O resultado é escrito no registrador de destino `rd`.

##### Sintaxe

A instrução SRL é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SRL.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000000` |  rs2  |  rs1  |  `101`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela SRL</b> - Tabela com sintaxe da instrução SRL.</p>

##### Formato

`srl rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] >> x[rs2]`

---

#### `SRLI` <Badge type="info" text="RV32I Base" />

Shift Right Logical Immediate (Deslocamento à Direita Lógico Imediato).

Desloca o valor armazenado no registrador `rs1` à direita pelo número de posições indicado
pelo `shamt`. Os _bits_ vazios de `rs1` são preenchidos com zeros. O resultado é
escrito no registrador de destino `rd`. Caso se decida atualizar o processador para uma
arquitetura de 64 bits, esta instrução terá sua sintaxe alterada (o shamt e o funct7 passam
a ter 6 bits cada).

##### Sintaxe

A instrução SRLI é do tipo I, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SRLI.

| Tipo |   31-26   | 24-20 | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :----: |
|  I   | `0000000` | shamt |  rs1  |  `101`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela SRLI</b> - Tabela com sintaxe da instrução SRLI.</p>

##### Formato

`srli rd, rs1, shamt`

##### Implementação

`x[rd] = x[rs1] >>shamt`

---

#### `SRA` <Badge type="info" text="RV32I Base" />

Shift Right Arithmetic (Deslocamento à Direita Aritmético).

Desloca o valor armazenado no registrador `rs1` à direita pelo número de posições indicado
pelos 5 _bits_ menos significativos do valor armazenado no registrador `rs2`. Os _bits_
remanescentes de `rs2` são ignorados. Os _bits_ vazios de `rs1` são preenchidos
com cópias do_bit_ mais significativo de `rs1`. O resultado é escrito no
registrador de destino `rd`.

##### Sintaxe

A instrução SRA é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SRA.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0100000` |  rs2  |  rs1  |  `101`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela SRA</b> - Tabela com sintaxe da instrução SRA.</p>

##### Formato

`sra rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] >> x[rs2]`

---

#### `SRAI` <Badge type="info" text="RV32I Base" />

Shift Right Arithmetic Immediate (Deslocamento à Direita Aritmético Imediato).

Desloca o valor armazenado no registrador `rs1` à direita pelo número de posições indicado
pelo `shamt`. Os _bits_ vazios de `rs1` são preenchidos com cópias do_bit_ mais
significativo de `rs1`. O resultado é escrito no registrador de destino `rd`. Caso se decida atualizar o 
processador para uma arquitetura de 64 bits, esta instrução terá sua sintaxe alterada (o shamt e o funct7 passam
a ter 6 bits cada).

##### Sintaxe

A instrução SRLI é do tipo I, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SRLI.

| Tipo |   31-26   | 25-20 | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :----: |
|  I   | `0100000` | shamt |  rs1  |  `101`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela SRAI</b> - Tabela com sintaxe da instrução SRAI.</p>

##### Formato

`srai rd, rs1, shamt`

##### Implementação

`x[rd] = x[rs1] >> shamt`

---

### Comparação

#### `SLT` <Badge type="info" text="RV32I Base" />

Set if Less Than (Definir se Menor que).

Verifica se o valor armazenado no registrador `rs1` é menor que o valor armazenado no 
registrador `rs2`, considerandoque são complemento de dois, em caso positivo, armazena 
1 no registrador de destino `rd`, caso contrário, armazena 0.

##### Sintaxe

A instrução SLT é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SLT.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000000` |  rs2  |  rs1  |  `010`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela SLT</b> - Tabela com sintaxe da instrução SLT.</p>

##### Formato

`slt rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] < x[rs2]`

---

#### `SLTI` <Badge type="info" text="RV32I Base" />

Set if Less Than Immediate (Definir se Menor que Imediato).

Verifica se o valor armazenado no registrador `rs1` é menor que o imediato com extensão de sinal,
considerando que são complemento de dois, em caso positivo, armazena 1 no
registrador de destino `rd`, caso contrário, armazena 0.

##### Sintaxe

A instrução SLTI é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela SLTI.

| Tipo |   31-20   | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :-----: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  `010`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela SLTI</b> - Tabela com sintaxe da instrução SLTI.</p>

##### Formato

`slti rd, rs1, immediate`

##### Implementação

`x[rd] = x[rs1] < sext(immediate)`

---

#### `SLTIU` <Badge type="info" text="RV32I Base" />

Set if Less Than Immediate Unisgned(Definir se Menor que Imediato Sem Sinal).

Verifica se o valor armazenado no registrador `rs1` é menor que o imediato com extensão de sinal,
considerando que são sem sinal, em caso positivo, armazena 1 no registrador de destino
`rd`, caso contrário, armazena 0.

##### Sintaxe

A instrução SLTIU é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela SLTIU.

| Tipo |   31-20   | 19-15 |  14-12  | 11-7 |  6-0   |
| :--: | :-------: | :---: | :-----: | :--: | :----: |
|  I   | imm[11:0] |  rs1  |  `011`  |  rd  | OP-IMM |
<p class="table_subtitle"><b>Tabela SLTIU</b> - Tabela com sintaxe da instrução SLTIU.</p>

##### Formato

`slti rd, rs1, immediate`

##### Implementação

`x[rd] = x[rs1] < sext(immediate)`

---

#### `SLTU` <Badge type="info" text="RV32I Base" />

Set if Less Than Unsigned(Definir se Menor que Sem Sinal).

Verifica se o valor armazenado no registrador `rs1` é menor que o valor armazenado no
registrador `rs2`, considerando que são valores sem sinal, em caso positivo, armazena 1 no 
registrador de destino `rd`, caso contrário, armazena 0.

##### Sintaxe

A instrução SLTU é do tipo R, tendo uma funct3 e uma funct7 próprias, como ilustrado na Tabela SLTU.

| Tipo |   31-25   | 24-20 | 19-15 |  14-12  | 11-7 | 6-0 |
| :--: | :-------: | :---: | :---: | :-----: | :--: | :-: |
|  R   | `0000000` |  rs2  |  rs1  |  `011`  |  rd  | OP  |
<p class="table_subtitle"><b>Tabela SLTU</b> - Tabela com sintaxe da instrução SLTU.</p>

##### Formato

`sltu rd, rs1, rs2`

##### Implementação

`x[rd] = x[rs1] < x[rs2]`

---

### Desvio Incondicional

#### `JAL` <Badge type="info" text="RV32I Base" />

Jump and Link (Salto e Link).

Escreve o endereço da próxima instrução (PC+4) no registrador de destino `rd` e modifica o
PC para o valor atual somado ao offset com extensão de sinal. Se `rd` for
omitido, o valor de retorno é armazenado em `x1`.

##### Sintaxe

A instrução JAL é do tipo J, tendo um opcode próprio, como ilustrado na Tabela JAL.

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11 - 7</th>
            <th style="text-align: center; white-space: nowrap;">6 - 0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">
                J
            </td>
            <td style="text-align: center;">
                offset[20|10:1|11|19:12]
            </td>
            <td style="text-align: center;">
                rd
            </td>
            <td style="text-align: center;">
                <code>1101111</code>
            </td>
        </tr>
    </tbody>
</table>
<p class="table_subtitle"><b>Tabela JAL</b> - Tabela com sintaxe da instrução JAL.</p>

##### Formato

`jal rd, offset`

##### Implementação

`x[rd] = pc+4; pc += sext(offset)`

---

#### `JALR` <Badge type="info" text="RV32I Base" />

Jump and Link Register (Salto e Link por Registrador).

Realiza um cópia do PC para `rs1 + sext(offset)`, mascara_bit_ menos
significativo do endereço resultante e armazena o endereço anterior de PC+4 no
registrador de destino `rd`. Se `rd` for omitido, o valor é armazenado em `x1`.

##### Sintaxe

A instrução JALR é do tipo I, tendo uma funct3 e um opcode próprios, como ilustrado na Tabela JALR.

| Tipo |    31-20     | 19-15 |  14-12  | 11-7 |    6-0    |
| :--: | :----------: | :---: | :-----: | :--: | :-------: |
|  I   | offset[11:0] |  rs1  |  `000`  |  rd  | `1100111` |
<p class="table_subtitle"><b>Tabela JALR</b> - Tabela com sintaxe da instrução JALR.</p>

##### Formato

`jalr rd, offset(rs1)`

##### Implementação

`t =pc+4; pc=(x[rs1]+sext(offset))&∼1; x[rd]=t`

---

### Desvio Condicional

#### `BEQ` <Badge type="info" text="RV32I Base" />

Branch if Equal (Desvio se Igual)

Verifica se o valor armazenado no registrador `rs1` é igual ao valor armazenado no registrador `rs2`, 
em caso positivo, modifica o PC para o valor atual somado ao offset com extensão de sinal.

##### Sintaxe

A instrução BEQ é do tipo B, tendo uma funct3 própria, como ilustrado na Tabela BEQ.

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31 - 25</th>
            <th style="text-align: center; white-space: nowrap;">24 - 20</th>
            <th style="text-align: center; white-space: nowrap;">19 - 15</th>
            <th style="text-align: center; white-space: nowrap;">14 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11 - 7</th>
            <th style="text-align: center; white-space: nowrap;">6 - 0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">
                B
            </td>
            <td style="text-align: center;">
                offset[12|10:5]
            </td>
            <td style="text-align: center;">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                <code>000</code>
            </td>
            <td style="text-align: center;">
                offset[4:1|11]
            </td>
            <td style="text-align: center;">
                BRANCH
            </td>
        </tr>
    </tbody>
</table> 
<p class="table_subtitle"><b>Tabela BEQ</b> - Tabela com sintaxe da instrução BEQ.</p>

##### Formato

`beq rs1, rs2, offset`

##### Implementação

`if (rs1 == rs2) pc += sext(offset)`

---

#### `BNE` <Badge type="info" text="RV32I Base" />

Branch if Not Equal (Desvio se Não Igual)

Verifica se o valor armazenado no registrador `rs1` é diferente do valor armazenado no registrador `rs2`, 
em caso positivo, modifica o PC para o valor atual somado ao offset com extensão de sinal.

##### Sintaxe

A instrução BNE é do tipo B, tendo uma funct3 própria, como ilustrado na Tabela BNE.

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31 - 25</th>
            <th style="text-align: center; white-space: nowrap;">24 - 20</th>
            <th style="text-align: center; white-space: nowrap;">19 - 15</th>
            <th style="text-align: center; white-space: nowrap;">14 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11 - 7</th>
            <th style="text-align: center; white-space: nowrap;">6 - 0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">
                B
            </td>
            <td style="text-align: center;">
                offset[12|10:5]
            </td>
            <td style="text-align: center;">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                <code>001</code>
            </td>
            <td style="text-align: center;">
                offset[4:1|11]
            </td>
            <td style="text-align: center;">
                BRANCH
            </td>
        </tr>
    </tbody>
</table>
<p class="table_subtitle"><b>Tabela BNE</b> - Tabela com sintaxe da instrução BNE.</p>

##### Formato

`bnq rs1, rs2, offset`

##### Implementação

`if (rs1 != rs2) pc += sext(offset)`

---

#### `BLT` <Badge type="info" text="RV32I Base" />

Branch if Less Than (Desvio se Menor que)

Verifica se o valor armazenado no registrador `rs1` é menor que o valor armazenado no 
registrador `rs2`, considerando que são números em complemento de dois, em caso positivo, 
modifica o PC para o valor atual somado ao offset com extensão de sinal.

##### Sintaxe

A instrução BLT é do tipo B, tendo uma funct3 própria, como ilustrado na Tabela BLT.

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31 - 25</th>
            <th style="text-align: center; white-space: nowrap;">24 - 20</th>
            <th style="text-align: center; white-space: nowrap;">19 - 15</th>
            <th style="text-align: center; white-space: nowrap;">14 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11 - 7</th>
            <th style="text-align: center; white-space: nowrap;">6 - 0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">
                B
            </td>
            <td style="text-align: center;">
                offset[12|10:5]
            </td>
            <td style="text-align: center;">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                <code>100</code>
            </td>
            <td style="text-align: center;">
                offset[4:1|11]
            </td>
            <td style="text-align: center;">
                BRANCH
            </td>
        </tr>
    </tbody>
</table>
<p class="table_subtitle"><b>Tabela BLT</b> - Tabela com sintaxe da instrução BLT.</p>

##### Formato

`blt rs1, rs2, offset`

##### Implementação

`if (rs1 < rs2) pc += sext(offset)`

---

#### `BGE` <Badge type="info" text="RV32I Base" />

Branch if Greater Than or Equal(Desvio se Maior ou Igual que)

Verifica se o valor armazenado no registrador `rs1` é maior ou igual ao valor armazenado no 
registrador `rs2`, considerando que são números em complemento de dois, em caso positivo, modifica
o PC para o valor atual somado ao offset com extensão de sinal.

##### Sintaxe

A instrução BGE é do tipo B, tendo uma funct3 própria, como ilustrado na Tabela BGE.

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31 - 25</th>
            <th style="text-align: center; white-space: nowrap;">24 - 20</th>
            <th style="text-align: center; white-space: nowrap;">19 - 15</th>
            <th style="text-align: center; white-space: nowrap;">14 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11 - 7</th>
            <th style="text-align: center; white-space: nowrap;">6 - 0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">
                B
            </td>
            <td style="text-align: center;">
                offset[12|10:5]
            </td>
            <td style="text-align: center;">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                <code>101</code>
            </td>
            <td style="text-align: center;">
                offset[4:1|11]
            </td>
            <td style="text-align: center;">
                BRANCH
            </td>
        </tr>
    </tbody>
</table>
<p class="table_subtitle"><b>Tabela BGE</b> - Tabela com sintaxe da instrução BGE.</p>

##### Formato

`bge rs1, rs2, offset`

##### Implementação

`if (rs1 >= rs2) pc += sext(offset)`

---

#### `BLTU` <Badge type="info" text="RV32I Base" />

Branch if Less Than Unsigned(Desvio se Menor que Sem Sinal)

Verifica se o valor armazenado no registrador `rs1` é menor ao valor armazenado no registrador `rs2`, 
considerando que são números sem sinal, em caso positivo, modifica o PC para o valor atual
somado ao offset com extensão de sinal.

##### Sintaxe

A instrução BLTU é do tipo B, tendo uma funct3 própria, como ilustrado na Tabela BLTU.

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31 - 25</th>
            <th style="text-align: center; white-space: nowrap;">24 - 20</th>
            <th style="text-align: center; white-space: nowrap;">19 - 15</th>
            <th style="text-align: center; white-space: nowrap;">14 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11 - 7</th>
            <th style="text-align: center; white-space: nowrap;">6 - 0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">
                B
            </td>
            <td style="text-align: center;">
                offset[12|10:5]
            </td>
            <td style="text-align: center;">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                <code>110</code>
            </td>
            <td style="text-align: center;">
                offset[4:1|11]
            </td>
            <td style="text-align: center;">
                BRANCH
            </td>
        </tr>
    </tbody>
</table>
<p class="table_subtitle"><b>Tabela BLTU</b> - Tabela com sintaxe da instrução BLTU.</p>

##### Formato

`bltu rs1, rs2, offset`

##### Implementação

`if (rs1 < rs2) pc += sext(offset)`

---

#### `BGEU` <Badge type="info" text="RV32I Base" />

Branch if Greater or Equal Than Unsigned(Desvio se Maior ou Igual que Sem Sinal)

Verifica se o valor armazenado no registrador `rs1` é maior ou igual ao valor armazenado no registrador `rs2`,
considerando que são números sem sinal, em caso positivo, modifica o PC para o
valor atual somado ao offset com extensão de sinal.

##### Sintaxe

A instrução BGEU é do tipo B, tendo uma funct3 própria, como ilustrado na Tabela BGEU.

<table>
    <thead>
        <tr>
            <th style="text-align: center; white-space: nowrap;">Tipo</th>
            <th style="text-align: center; white-space: nowrap;">31 - 25</th>
            <th style="text-align: center; white-space: nowrap;">24 - 20</th>
            <th style="text-align: center; white-space: nowrap;">19 - 15</th>
            <th style="text-align: center; white-space: nowrap;">14 - 12</th>
            <th style="text-align: center; white-space: nowrap;">11 - 7</th>
            <th style="text-align: center; white-space: nowrap;">6 - 0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">
                B
            </td>
            <td style="text-align: center;">
                offset[12|10:5]
            </td>
            <td style="text-align: center;">
                rs2
            </td>
            <td style="text-align: center;">
                rs1
            </td>
            <td style="text-align: center;">
                <code>111</code>
            </td>
            <td style="text-align: center;">
                offset[4:1|11]
            </td>
            <td style="text-align: center;">
                BRANCH
            </td>
        </tr>
    </tbody>
</table>
<p class="table_subtitle"><b>Tabela BGEU</b> - Tabela com sintaxe da instrução BGEU.</p>

##### Formato

`bgeu rs1, rs2, offset`

##### Implementação

`if (rs1 >= rs2) pc += sext(offset)`

---

### Busca na Memória

#### `LB` <Badge type="info" text="RV32I Base" />

Load Byte (Carrega Byte).

Carrega um byte da memória no endereço `rs1 + sext(offset)` e armazena o valor
no registrador de destino `rd`, com extensão de sinal.

##### Sintaxe

A instrução LB é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela LB.

| Tipo |    31-20     | 19-15 |  14-12  | 11-7 | 6-0  |
| :--: | :----------: | :---: | :-----: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  `000`  |  rd  | LOAD |
<p class="table_subtitle"><b>Tabela LB</b> - Tabela com sintaxe da instrução LB.</p>

##### Formato

`lb rd, offset(rs1)`

##### Implementação

`x[rd] = sext(M[x[rs1] + sext(offset)][7:0])`

---

#### `LH` <Badge type="info" text="RV32I Base" />

Load Halfword (Carrega Halfword).

Carrega dois bytes da memória no endereço `rs1 + sext(offset)` e armazena o
valor no registrador de destino `rd`, com extensão de sinal.

##### Sintaxe

A instrução LH é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela LH.

| Tipo |    31-20     | 19-15 |  14-12  | 11-7 | 6-0  |
| :--: | :----------: | :---: | :-----: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  `001`  |  rd  | LOAD |
<p class="table_subtitle"><b>Tabela LH</b> - Tabela com sintaxe da instrução LH.</p>

##### Formato

`lh rd, offset(rs1)`

##### Implementação

`x[rd] = sext(M[x[rs1] + sext(offset)][15:0])`

---

#### `LBU` <Badge type="info" text="RV32I Base" />

Load Byte Unsigned(Carrega Byte Sem Sinal).

Carrega um byte da memória no endereço `rs1 + sext(offset)` e armazena o valor
no registrador de destino `rd`, com extensão de zero.

##### Sintaxe

A instrução LBU é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela LBU.

| Tipo |    31-20     | 19-15 |  14-12  | 11-7 | 6-0  |
| :--: | :----------: | :---: | :-----: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  `100`  |  rd  | LOAD |
<p class="table_subtitle"><b>Tabela LBU</b> - Tabela com sintaxe da instrução LBU.</p>

##### Formato

`lbu rd, offset(rs1)`

##### Implementação

`x[rd] = M[x[rs1] + sext(offset)][7:0]`

---

#### `LHU` <Badge type="info" text="RV32I Base" />

Load Halfword Unsigned(Carrega Halfword Sem Sinal).

Carrega dois bytes da memória no endereço `rs1 + sext(offset)` e armazena o
valor no registrador de destino `rd`, com extensão de zero.

##### Sintaxe

A instrução LHU é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela LHU.

| Tipo |    31-20     | 19-15 |  14-12  | 11-7 | 6-0  |
| :--: | :----------: | :---: | :-----: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  `101`  |  rd  | LOAD |
<p class="table_subtitle"><b>Tabela LHU</b> - Tabela com sintaxe da instrução LHU.</p>

##### Formato

`lhu rd, offset(rs1)`

##### Implementação

`x[rd] = M[x[rs1] + sext(offset)][15:0]`

---

#### `LW` <Badge type="info" text="RV32I Base" />

Load Word (Carrega Word).

Carrega quatro bytes da memória no endereço `rs1 + sext(offset)` e armazena o
valor no registrador de destino `rd`.

##### Sintaxe

A instrução LW é do tipo I, tendo uma funct3 própria, como ilustrado na Tabela LW.

| Tipo |    31-20     | 19-15 |  14-12  | 11-7 | 6-0  |
| :--: | :----------: | :---: | :-----: | :--: | :--: |
|  I   | offset[11:0] |  rs1  |  `010`  |  rd  | LOAD |
<p class="table_subtitle"><b>Tabela LW</b> - Tabela com sintaxe da instrução LW.</p>

##### Formato

`lw rd, offset(rs1)`

##### Implementação

`x[rd] = sext(M[x[rs1] + sext(offset)][31:0])`

---

### Escrita na Memória

#### `SB` <Badge type="info" text="RV32I Base" />

Store Byte (Armazena Byte).

Armazena o byte menos significativo do valor armazenado no registrador `rs2` na memória no endereço
`rs1 + sext(offset)`.

##### Sintaxe

A instrução SB é do tipo S, tendo uma funct3 própria, como ilustrado na Tabela SB.

| Tipo |    31-25     | 24-20 | 19-15 |  14-12  |    11-7     |  6-0  |
| :--: | :----------: | :---: | :---: | :-----: | :---------: | :---: |
|  S   | offset[11:5] |  rs2  |  rs1  |  `000`  | offset[4:0] | STORE |
<p class="table_subtitle"><b>Tabela SB</b> - Tabela com sintaxe da instrução SB.</p>

##### Formato

`sb rs2, offset(rs1)`

##### Implementação

`M[x[rs1] + sext(offset)] = x[rs2][7:0]`

---

#### `SH` <Badge type="info" text="RV32I Base" />

Store Halfword (Armazena Halfword).

Armazena os dois bytes menos significativo do valor armazenado no registrador `rs2` na memória no
endereço `rs1 + sext(offset)`.

##### Sintaxe

A instrução SH é do tipo S, tendo uma funct3 própria, como ilustrado na Tabela SH.

| Tipo |    31-25     | 24-20 | 19-15 |  14-12  |    11-7     |  6-0  |
| :--: | :----------: | :---: | :---: | :-----: | :---------: | :---: |
|  S   | offset[11:5] |  rs2  |  rs1  |  `001`  | offset[4:0] | STORE |
<p class="table_subtitle"><b>Tabela SH</b> - Tabela com sintaxe da instrução SH.</p>

##### Formato

`sh rs2, offset(rs1)`

##### Implementação

`M[x[rs1] + sext(offset)] = x[rs2][15:0]`

---

#### `SW` <Badge type="info" text="RV32I Base" />

Store Word (Armazena Word).

Armazena os quatro bytes menos significativo do valor armazenado no registrador `rs2` na memória no
endereço `rs1 + sext(offset)`.

##### Sintaxe

A instrução SW é do tipo S, tendo uma funct3 própria, como ilustrado na Tabela SW.

| Tipo |    31-25     | 24-20 | 19-15 |  14-12  |    11-7     |  6-0  |
| :--: | :----------: | :---: | :---: | :-----: | :---------: | :---: |
|  S   | offset[11:5] |  rs2  |  rs1  |  `010`  | offset[4:0] | STORE |
<p class="table_subtitle"><b>Tabela SW</b> - Tabela com sintaxe da instrução SW.</p>

##### Formato

`sw rs2, offset(rs1)`

##### Implementação

`M[x[rs1] + sext(offset)] = x[rs2][31:0]`
