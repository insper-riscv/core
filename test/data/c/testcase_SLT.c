void main() __attribute__((noreturn));

void main() {
    asm("addi  x4, x0,      1");
    asm("lui   x9,     262144");
    asm("addi  x1, x0,      8");
    asm("addi  x2, x0,      7");
    asm("addi  x3, x0,      9");
    asm("lui  x10,     524288");
    asm("slt  x20, x1,     x3");
    asm("slt  x20, x1,     x2");
    asm("slt  x20, x2,     x3");
    asm("slt  x20, x4,     x9");
    asm("slt  x20, x4,    x10");
}
