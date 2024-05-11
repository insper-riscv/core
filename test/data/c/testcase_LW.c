void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0,   8    ");
    asm("addi x2, x0, 8");
    asm("sw x2, 0(x1)");
    asm("lw x3, 0(x1)");
    asm("addi x4, x3, 4");
    asm("addi x0, x0, 0");
    asm("addi x0, x0, 0");
    asm("addi x0, x0, 0");
    asm("addi x5, x4, 4");
    asm("addi x6, x0, 8");
    asm("lw x7, 0(x1)");
    asm("beq x6, x7, j_eq1");
    asm("addi x9, x0, 7");
    asm("addi x9, x0, 8");
    asm("j_eq1:");
    asm("addi x9, x0, 12");
    asm("addi x9, x0, 16");
    asm("addi x10, x0, 8");
    asm("beq x6, x10, j_eq2");
    asm("addi x9, x0, 9");
    asm("addi x9, x0, 8");
    asm("j_eq2:");
    asm("addi x9, x0, 12");
    asm("addi x9, x0, 16");
    asm("nop");
    asm("nop");
    asm("nop");
}
