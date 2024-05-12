    .section    .text
    .globl      main

main:
    addi        x1,         x0,         0       ;
    lui         x1,         1048064             ;
    ori         x2,         x1,         7       ;
    ori         x2,         x1,         7       ;
    addi        x0,         x0,         0       ;
    ori         x2,         x1,         7       ;
    nop                                         ;
    nop                                         ;
    nop                                         ;
