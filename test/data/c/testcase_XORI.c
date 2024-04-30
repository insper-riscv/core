void main() __attribute__((noreturn));

void main() {
    asm("lui  x1,     1048064");
    asm("xori x2, x1,       7");
    asm("xori x2, x1,       7");
    asm("addi x0, x0,       0");
    asm("xori x2, x1,       7");
}
