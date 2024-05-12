    .section    .text
    .globl      main

main:
    addi        x1,         x0,         0       ;
    lui         x1,         1048064             ;
    xori        x2,         x1,         7       ;
    xori        x2,         x1,         7       ;
    addi        x0,         x0,         0       ;
    xori        x2,         x1,         7       ;
    nop                                         ;
    nop                                         ;
    nop                                         ;
