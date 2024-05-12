    .section    .text
    .globl      main

main:
    addi        x1,         x0,         0       ;
    jal         x7,         j_al1               ;
    addi        x0,         x0,         0       ;
    addi        x2,         x0,         8       ;
    addi        x2,         x0,         12      ;
    addi        x2,         x0,         16      ;
j_al1:
    addi        x2,         x0,         17      ;
    jal         x7,         j_al2               ;
    addi        x0,         x0,         0       ;
    addi        x2,         x0,         8       ;
j_al2:
    addi        x2,         x0,         12      ;
    addi        x2,         x0,         16      ;
    addi        x2,         x0,         17      ;
    nop                                         ;
    nop                                         ;
    nop                                         ;
