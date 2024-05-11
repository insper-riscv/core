void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0,   0");
    asm("addi x1, x0,   1");
    asm("addi x1, x0,   2");
    asm("addi x1, x0,   4");
    asm("addi x1, x0,   8");
    asm("addi x1, x0,  16");
    asm("addi x1, x0,  32");
    asm("addi x1, x0,  64");
    asm("addi x1, x0, 128");
    asm("addi x1, x0, 256");
    asm("addi x2, x1,   1");
    asm("nop");
    asm("nop");
    asm("nop");
    asm("nop");

}
