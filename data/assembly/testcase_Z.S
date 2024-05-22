    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    add         x3,         x1,         x1      ;
    addi        x1,         x0,         0       ;
    and         x5,         x3,         x3      ;
    andi        x1,         x0,         7       ;
    auipc       x8,         1                   ;
    beq         x1,         x0,         j_eq    ;
    bge         x2,         x1,         j_ge    ;
    bgeu        x2,         x1,         j_geu   ;
    blt         x1,         x2,         j_lt    ;
j_eq:
j_ge:
    bltu        x1,         x2,         j_ltu   ;
j_geu:
    bne         x1,         x2,         j_ne    ;
j_lt:
    jal         x7,         j_al                ;
j_ltu:
    jalr        x2,         20(x1)              ;
j_ne:
    lb          x3,         0(x1)               ;
j_al:
    lbu         x3,         0(x1)               ;
    lh          x3,         0(x1)               ;
    lhu         x3,         0(x1)               ;
    lui         x8,         1                   ;
    lw          x3,         0(x1)               ;
    or          x3,         x0,         x1      ;
    ori         x2,         x1,         7       ;
    sb          x2,         0(x1)               ;
    sh          x2,         0(x1)               ;
    sll         x3,         x1,         x2      ;
    slli        x2,         x1,         4       ;
    slt         x20,        x1,         x3      ;
    slti        x2,         x10,        1       ;
    sltiu       x2,         x10,        1       ;
    sltu        x20,        x4,         x10     ;
    sra         x3,         x9,         x2      ;
    srai        x3,         x9,         6       ;
    srl         x3,         x1,         x2      ;
    srli        x2,         x1,         6       ;
    sub         x3,         x3,         x2      ;
    sw          x2,         0(x1)               ;
    xor         x3,         x2,         x2      ;
    xori        x2,         x1,         7       ;
