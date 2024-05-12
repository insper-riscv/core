    .section    .text
    .globl      main

main:
    addi        x1,         x0,         0       ;
    jalr        x1,         12(x0)              ;
    addi        x0,         x0,         0       ;
    addi        x2,         x0,         8       ;
    addi        x1,         x1,         12      ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    jalr        x2,         20(x1)              ;
    addi        x0,         x0,         0       ;
    addi        x2,         x0,         8       ;
    addi        x2,         x1,         12      ;
    nop                                         ;
    nop                                         ;
    nop                                         ;
