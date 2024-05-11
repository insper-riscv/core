void main() __attribute__((noreturn));

void main() {
    asm("lui  x1,     1048064");
    asm("ori  x2, x1,       7");
    asm("ori  x2, x1,       7");
    asm("addi x0, x0,       0");
    asm("ori  x2, x1,       7");
    asm("nop");
    asm("nop");
    asm("nop");
}
