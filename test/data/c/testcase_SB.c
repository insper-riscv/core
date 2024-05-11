void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0,   8    ");
    asm("addi x2, x0, 639    ");
    asm("addi x0, x0,   0    ");
    asm("addi x0, x0,   0    ");
    asm("addi x0, x0,   0    ");
    asm("sw   x0,       0(x1)");
    asm("sb   x2,       0(x1)");
    asm("lw   x3,       0(x1)");
    asm("addi x0, x0,   0    ");
    asm("addi x0, x0,   0    ");
    asm("addi x0, x0,   0    ");
    asm("addi x4, x3,   2    ");
    asm("nop");
    asm("nop");
    asm("nop");
}
