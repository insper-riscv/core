    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         7       ;
    andi        x2,         x1,         6       ;
    andi        x2,         x1,         5       ;
    addi        x0,         x0,         0       ;
    andi        x2,         x1,         7       ;
