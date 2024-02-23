# Arquitetura de instruções RISC-V

RISC (Reduced Instruction Set Computer), é um termo geral para se referir a
computadores cujas CPUs (Core Processing Units) foram projetadas para
interpretar instruções uniformes mais otimizadas, ou seja, instruções mais
simples e menores. RISC-V, o objeto de desenvolvimento deste projeto, é uma
variação aberta ao público da arquitetura RISC, ou seja, uma arquitetura
disponível para o desenvolvimento sem a necessidade de pagar royalties.

## Especificação RV32I ISA

Embora o comum seja se referir ao RISC-V como sendo uma arquitetura RISC, na
verdade ele é uma família de arquiteturas de conjuntos de instruções (ISA), com
quatro arquiteturas base. No caso deste projeto, foi acordado trabalhar
desenvolvendo a arquitetura base de instruções de inteiros de 32 bits, a RV32I
(RV sendo a nominação padrão de arquiteturas RISC-V, 32 indicando o tamanho das
instruções, e I indicando que a arquitetura base é a dos Inteiros) As seguintes
instruções foram implementadas:

| Categoria     | Nome                            | Tipo | Sintaxe               |
| ------------- | ------------------------------- | ---- | --------------------- |
| Shifts        | Shift Left Logical              | R    | `SLL rd, rs1, rs2`    |
|               | Shift Left Log. Imm.            | I    | `SLLI rd, rs1, shamt` |
|               | Shift Right Logical             | R    | `SRL rd, rs1, rs2`    |
|               | Shift Right Log. Imm.           | I    | `SRLI rd, rs1, shamt` |
|               | Shift Right Arithmetic          | R    | `SRA rd, rs1, rs2`    |
|               | Shift Right Arith. Imm.         | I    | `SRAI rd, rs1, shamt` |
| Arithmetic    | Add                             | R    | `ADD rd, rs1, rs2`    |
|               | Add Immediate                   | I    | `ADDI rd, rs1, imm`   |
|               | Subtract                        | R    | `SUB rd, rs1, rs2`    |
|               | Load Upper Immediate            | U    | `LUI rd, imm`         |
|               | Add Upper Imm. to PC            | U    | `AUIPC rd, imm`       |
| Logical       | Xor                             | R    | `XOR rd, rs1, rs2`    |
|               | Xor Immediate                   | I    | `XORI rd, rs1, imm`   |
|               | Or                              | R    | `OR rd, rs1, rs2`     |
|               | Or Immediate                    | I    | `ORI rd, rs1, imm`    |
|               | And                             | R    | `AND rd, rs1, rs2`    |
|               | And Immediate                   | I    | `ANDI rd, rs1, imm`   |
| Compare       | Set if Less Than                | R    | `SLT rd, rs1, rs2`    |
|               | Set if Less Than Imm.           | I    | `SLTI rd, rs1, imm`   |
|               | Set if Less Than Unsigned       | R    | `SLTU rd, rs1, rs2`   |
|               | Set if Less Than Imm. Uns.      | I    | `SLTI rd, rs1, imm`   |
| Branches      | Branch if Equal                 | B    | `BEQ rs1, rs2, imm`   |
|               | Branch if Not Equal             | B    | `BNE rs1, rs2, imm`   |
|               | Branch if Less Than             | B    | `BLT rs1, rs2, imm`   |
|               | Branch if Greater or Equal      | B    | `BGE rs1, rs2, imm`   |
|               | Branch if Less Than Uns.        | B    | `BLTU rs1, rs2, imm`  |
|               | Branch if Greater or Equal Uns. | B    | `BGEU rs1, rs2, imm`  |
| Jump and Link | Jump and Link                   | J    | `JAL rd, imm`         |
|               | Jump and Link Register          | I    | `JALR rd, rs1, imm`   |
| Synch         | Synch thread                    | I    | `FENCE`               |
|               | Synch Instruction and Data      | I    | `FENCE.I`             |
| Enviroment    | Call                            | I    | `ECALL`               |
|               | Break                           | I    | `EBREAK`              |
| Loads         | Load Byte                       | I    | `LB rd, rs1, imm`     |
|               | Load Halfword                   | I    | `LH rd, rs1, imm`     |
|               | Load Byte Unsigned              | I    | `LBU rd, rs1, imm`    |
|               | Load Half Unsigned              | I    | `LHU rd, rs1, imm`    |
|               | Load Word                       | I    | `LW rd, rs1, imm`     |
| Stores        | Store Byte                      | S    | `SB rs1, rs2, imm`    |
|               | Store Halfword                  | S    | `SH rs1, rs2, imm`    |
|               | Store Word                      | S    | `SW rs1, rs2, imm`    |

A coluna `tipo` indica o formato da instrução em bites para sintaxe assembly.
Segue a especificação oficial:

![Formato das Instruções](/images/image_instruction.drawio.png)

## Especificação da expansão RV32IM ISA

Além do conjunto de instruções base, pode-se incrementar o conjunto de
instruções da arquiteura RISC-V com com expansões modulares. Para este projeto,
será implementada a expansão M, tornando o processador um RV32IM (processador
RISC-V de 32 bits para inteiros com extensão para multiplicação e divisão).

| Categoria | Nome                   | Tipo | Sintaxe               |
| --------- | ---------------------- | ---- | --------------------- |
| Multiply  | Multiply               | R    | `MUL rd, rs1, rs2`    |
|           | Multiply High          | R    | `MULH rd, rs1, rs2`   |
|           | Multiply High Sign/Uns | R    | `MULHSU rd, rs1, rs2` |
|           | Multiply High Uns      | R    | `MULHU rd, rs1, rs2`  |
| Divide    | Divide                 | R    | `DIV rd, rs1, rs2`    |
|           | Divide Unsigned        | R    | `DIVU rd, rs1, rs2`   |
| Remainder | Remainder              | R    | `REM rd, rs1, rs2`    |
|           | Remainder Unsigned     | R    | `REMU rd, rs1, rs2`   |

## Arquitetura do processador

A partir do núcleo de processamento, é possível implementar periféricos que
adicionam funcionalidade. Segue o diagrama de barramentos de comunicação entre o
núcleo `CORE` e alguns dos periféricos planejados para este projeto.

![Periféricos](/images/infra.drawio.png)

O núcleo de processamento é organizado em pipeline com 5 etapas, sem uso de
barramento, cache ou controlador de memória.

![Núcleo de processamento com pipeline](/images/risc-v.drawio.png)

## Referências:

- Hennessy, J. L.; Patterson, D. A. (2020) 
**Computer Organization and Design: The Hardware/Software Interface (RISC-V Edition)**. p. 314.

- Patterson, David A.; Waterman, Andrew. **The RISC-V reader: An open architecture atlas**.
 Strawberry Canyon LLC, 2017.

- “The RISC-V Instruction Set Manual, Volume I: User-Level ISA, Document Version
  20191213”, Editors Andrew Waterman and Krste Asanovic, RISC-V Foundation,
  December 2019.

- Wright, A. **What Is RISC, What Is RISC V, and How Do They Differ?**.
  MakeUseOf, 15 oct. 2022. Available at:
  https://www.makeuseof.com/what-is-risc-what-is-risc-v-how-do-they-differ/

- **GLOSSARY - Instruction Set Architecture: What Is an Instruction Set Architecture?**.
 ARM, 14 nov. 2023. Available at:  https://www.arm.com/glossary/isa
