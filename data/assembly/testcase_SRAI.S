    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         256     ;
    srai        x2,         x1,         6       ;
    srai        x2,         x1,         6       ;
    lui         x8,         1                   ;
    srai        x2,         x8,         6       ;
    srai        x2,         x8,         6       ;
    lui         x9,         524288              ;
    srai        x3,         x9,         6       ;
    srai        x3,         x9,         6       ;
    srai        x2,         x1,         6       ;
    srai        x2,         x8,         6       ;
    srai        x3,         x9,         6       ;
