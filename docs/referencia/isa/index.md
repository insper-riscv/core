# Conjunto de Instruções

As instruções são sequências de instruções em binário de 32 bits. Cada tipo de
instrução reserva sua sintaxe seguindo os seguintes segmentos.

- `opcode`: Codifica o tipo de instrução ou uma instrução específica;
- `funct3`: Codifica a operacionalização da instrução;
- `funct7`: Codifica uma variação da operacionalização;
- `rs1`: Endereça registrador de recurso primário;
- `rs2`: Endereça registrador de recurso secundário;
- `rd`: Endereça registrador de destinação;
- `imm`: Codifica valor do imediato.

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

## Instruções

---

### `LUI`

Load Upper Immediate (Carregar Superior Imediato).

Carrega constantes de 32 bits. `LUI` coloca o valor imediato nos 20 bits
superiores do registrador `rd`, preenchendo os 12 bits mais baixos com zeros.

#### Sintaxe

| Tipo |   31-12    | 11-7 |   6-0   |
| :--: | :--------: | :--: | :-----: |
|  U   | imm[31:12] |  rd  | 0110111 |

#### Formato

`lui rd, imm`

#### Implementação

`x[rd] = imm[31:12] << 12`
