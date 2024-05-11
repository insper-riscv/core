void main() __attribute__((noreturn));

void main() {
    asm("addi x2, x0,  2");
    asm("addi x1, x1,  1");
    asm("addi x7, x0,  7");
    asm("addi x7, x0,  7");
    asm("addi x7, x0,  7");
    asm("bge  x2, x1, j_ge");
    asm("addi x0, x0,  0");
    asm("addi x3, x0,  8");
    asm("j_ge:");
    asm("addi x3, x0,  4");
    asm("nop");
    asm("nop");
    asm("nop");
}
