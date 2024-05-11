void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0,    256");
    asm("addi x2, x0,      6");
    asm("sra  x3, x1,     x2");
    asm("lui  x8,          1");
    asm("addi x0, x0,      0");
    asm("sra  x3, x8,     x2");
    asm("lui  x9,     524288");
    asm("sra  x3, x9,     x2");
    asm("nop");
    asm("nop");
    asm("nop");
}
