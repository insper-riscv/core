    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x0,         x0,         0       ;
    addi        x1,         x0,         8       ;
    addi        x2,         x0,         8       ;
    sw          x2,         0(x1)               ;
    lw          x3,         0(x1)               ;
    addi        x4,         x3,         4       ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    addi        x5,         x4,         4       ;
    addi        x6,         x0,         8       ;
    lw          x7,         0(x1)               ;
    beq         x6,         x7,         j_eq1   ;
    addi        x9,         x0,         7       ;
    addi        x9,         x0,         8       ;
j_eq1:
    addi        x9,         x0,         12      ;
    addi        x9,         x0,         16      ;
    addi        x10,        x0,         8       ;
    beq         x6,         x10,        j_eq2   ;
    addi        x9,         x0,         9       ;
    addi        x9,         x0,         8       ;
j_eq2:
    addi        x9,         x0,         12      ;
    addi        x9,         x0,         16      ;
