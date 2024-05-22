    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         256     ;
    addi        x2,         x0,         6       ;
    sra         x3,         x1,         x2      ;
    lui         x8,         1                   ;
    addi        x0,         x0,         0       ;
    sra         x3,         x8,         x2      ;
    lui         x9,         524288              ;
    sra         x3,         x9,         x2      ;
