    .section    .text
    .globl      main

main:
    addi        x1,         x0,         0       ;
    mulhu       x3,         x2,         x1      ;
    mulhu       x3,         x2,         x1      ;
    mulhu       x3,         x2,         x1      ;
    mulhu       x3,         x2,         x1      ;
    nop                                         ;
    nop                                         ;
    nop                                         ;
