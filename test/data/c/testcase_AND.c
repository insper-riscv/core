void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0,  7");
    asm("addi x2, x0,  6");
    asm("addi x3, x0,  5");
    asm("addi x0, x0,  0");
    asm("addi x0, x0,  0");
    asm("addi x0, x0,  0");
    asm("and  x5, x2, x1");
    asm("and  x5, x3, x1");
    asm("and  x5, x3, x2");
    asm("and  x5, x3, x3");
}
