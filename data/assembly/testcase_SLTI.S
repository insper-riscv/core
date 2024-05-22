    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    lui         x10,        524288              ;
    addi        x1,         x0,         8       ;
    slti        x2,         x1,         7       ;
    slti        x2,         x1,         9       ;
    lui         x9,         262144              ;
    slti        x2,         x1,         4       ;
    slti        x2,         x1,         10      ;
    slti        x2,         x1,         40      ;
    slti        x2,         x9,         1       ;
    slti        x2,         x10,        1       ;
