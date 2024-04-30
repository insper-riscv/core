void main() __attribute__((noreturn));

void main() {
    asm("jalr x1,     12(x0)");
    asm("addi x0, x0,  0    ");
    asm("addi x2, x0,  8    ");
    asm("addi x1, x1, 12    ");
    asm("addi x0, x0,  0    ");
    asm("addi x0, x0,  0    ");
    asm("addi x0, x0,  0    ");
    asm("jalr x2,     20(x1)");
    asm("addi x0, x0,  0    ");
    asm("addi x2, x0,  8    ");
    asm("addi x2, x1, 12    ");
}
