    .section    .text
    .globl      main

main:
    addi        x1,         x0,         0       ;
    beq         x1,         x0,         j_eq    ;
    addi        x0,         x0,         0       ;
    addi        x3,         x0,         8       ;
    addi        x3,         x0,         4       ;
j_eq:
    addi        x3,         x0,         2       ;
    addi        x3,         x0,         1       ;
    nop                                         ;
    nop                                         ;
    nop                                         ;
