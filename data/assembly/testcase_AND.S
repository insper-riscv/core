    .section    .text
    .globl      main

main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         7       ;
    addi        x2,         x0,         6       ;
    addi        x3,         x0,         5       ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    and         x5,         x2,         x1      ;
    and         x5,         x3,         x1      ;
    and         x5,         x3,         x2      ;
    and         x5,         x3,         x3      ;
    nop                                         ;
    nop                                         ;
    nop                                         ;
