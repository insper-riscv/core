    .section    .text
    .globl      _start
    .globl      main
_start:
main:
    addi        x1,         x0,         0       ;
    addi        x1,         x0,         8       ;
    addi        x2,         x0,         639     ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    sw          x0,         0(x1)               ;
    sb          x2,         0(x1)               ;
    lw          x3,         0(x1)               ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    addi        x0,         x0,         0       ;
    addi        x4,         x3,         2       ;
