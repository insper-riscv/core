    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x2,         x0,         2       ;
    addi        x1,         x1,         1       ;
    addi        x7,         x0,         7       ;
    addi        x7,         x0,         7       ;
    addi        x7,         x0,         7       ;
    bltu        x1,         x2,         j_ltu   ;
    addi        x0,         x0,         0       ;
    addi        x3,         x0,         8       ;
j_ltu:
    addi        x3,         x0,         4       ;
