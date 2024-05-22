    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         8       ;
    add         x3,         x1,         x1      ;
    add         x3,         x1,         x1      ;
    addi        x0,         x0,         0       ;
    add         x3,         x1,         x1      ;
    add         x3,         x1,         x1      ;
    add         x3,         x1,         x1      ;
