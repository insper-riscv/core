    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    lui         x10,        524288              ;
    addi        x1,         x0,         8       ;
    sltiu       x2,         x1,         7       ;
    sltiu       x2,         x1,         9       ;
    lui         x9,         262144              ;
    sltiu       x2,         x1,         4       ;
    sltiu       x2,         x1,         10      ;
    sltiu       x2,         x1,         40      ;
    sltiu       x2,         x9,         1       ;
    sltiu       x2,         x10,        1       ;
