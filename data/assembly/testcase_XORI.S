    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    lui         x1,         1048064             ;
    xori        x2,         x1,         7       ;
    xori        x2,         x1,         7       ;
    addi        x0,         x0,         0       ;
    xori        x2,         x1,         7       ;
