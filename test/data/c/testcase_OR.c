void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0,       7");
    asm("lui  x2,     1048064");
    asm("or   x3, x2,      x1");
    asm("addi x0, x0,       0");
    asm("or   x3, x0,      x1");
    asm("nop");
    asm("nop");
    asm("nop");
}
