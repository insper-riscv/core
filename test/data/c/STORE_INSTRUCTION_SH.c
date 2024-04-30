void main() __attribute__((noreturn));

void main() {
    asm("lui  x2,      24    ");
    asm("addi x1, x0,   8    ");
    asm("addi x2, x2, 639    ");
    asm("addi x0, x0,   0    ");
    asm("addi x0, x0,   0    ");
    asm("addi x0, x0,   0    ");
    asm("sw   x0,       0(x1)");
    asm("sh   x2,       0(x1)");
    asm("lw   x3,       0(x1)");
    asm("addi x0, x0,   0    ");
    asm("addi x0, x0,   0    ");
    asm("addi x0, x0,   0    ");
    asm("addi x4, x3,   2    ");
}
