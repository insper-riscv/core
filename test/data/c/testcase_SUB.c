void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 8");
    asm("addi x2, x0, 2");
    asm("addi x0, x0, 0");
    asm("addi x0, x0, 0");
    asm("addi x0, x0, 0");
    asm("sub x3, x1, x2");
    asm("sub x3, x3, x2");
    asm("sub x3, x3, x2");
    asm("sub x3, x3, x2");
}
