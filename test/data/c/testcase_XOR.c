void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0,       7");
    asm("lui  x2,     1048064");
    asm("xor  x3, x2,      x1");
    asm("addi x0, x0,       0");
    asm("addi x0, x0,       0");
    asm("xor  x3, x2,      x1");
    asm("xor  x3, x1,      x1");
    asm("xor  x3, x2,      x2");
    asm("nop");
    asm("nop");
    asm("nop");
}
