void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 0");
    asm("jal  x7,     20");
    asm("addi x0, x0,  0");
    asm("addi x2, x0,  8");
    asm("addi x2, x0, 12");
    asm("addi x2, x0, 16");
    asm("addi x2, x0, 17");
    asm("jal  x7,     j_al");
    asm("addi x0, x0,  0");
    asm("addi x2, x0,  8");
    asm("j_al:");
    asm("addi x2, x0, 12");
    asm("addi x2, x0, 16");
    asm("addi x2, x0, 17");
    asm("nop");
    asm("nop");
    asm("nop");
}
