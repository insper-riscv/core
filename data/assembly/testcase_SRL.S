    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         256     ;
    addi        x2,         x0,         6       ;
    srl         x3,         x1,         x2      ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    srl         x3,         x1,         x2      ;
    srl         x3,         x1,         x2      ;
    srl         x3,         x1,         x2      ;
