    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         7       ;
    addi        x2,         x0,         8       ;
    addi        x1,         x1,         16      ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    addi        x1,         x1,         4       ;
    jalr        x2,         20(x1)              ;
    addi        x0,         x0,         0       ;
    addi        x2,         x0,         8       ;
    addi        x2,         x1,         12      ;
