    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         7       ;
    lui         x2,         1048064             ;
    xor         x3,         x2,         x1      ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    xor         x3,         x2,         x1      ;
    xor         x3,         x1,         x1      ;
    xor         x3,         x2,         x2      ;
