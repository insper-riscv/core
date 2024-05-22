    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         8       ;
    slli        x2,         x1,         4       ;
    slli        x2,         x1,         4       ;
    addi        x0,         x0,         0       ;
    slli        x2,         x1,         4       ;
