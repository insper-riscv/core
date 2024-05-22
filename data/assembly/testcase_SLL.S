    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         8       ;
    addi        x2,         x0,         8       ;
    sll         x3,         x1,         x2      ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    sll         x3,         x1,         x2      ;
