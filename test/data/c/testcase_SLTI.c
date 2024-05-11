void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 0");
    asm("lui  x10,      524288");
    asm("addi  x1,  x0,      8");
    asm("slti  x2,  x1,      7");
    asm("slti  x2,  x1,      9");
    asm("lui   x9,      262144");
    asm("slti  x2,  x1,      4");
    asm("slti  x2,  x1,     10");
    asm("slti  x2,  x1,     40");
    asm("slti  x2,  x9,      1");
    asm("slti  x2, x10,      1");
    asm("nop");
    asm("nop");
    asm("nop");
}
