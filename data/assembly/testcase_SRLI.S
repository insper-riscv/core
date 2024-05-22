    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         256     ;
    srli        x2,         x1,         6       ;
    srli        x2,         x1,         6       ;
    addi        x0,         x0,         0       ;
    srli        x2,         x1,         6       ;
    srli        x2,         x1,         6       ;
