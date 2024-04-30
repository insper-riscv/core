void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 8");
    asm("add x3, x1, x1");
    asm("add x3, x1, x1");
    asm("addi x0, x0, 0");
    asm("add x3, x1, x1");
    asm("add x3, x1, x1");
    asm("add x3, x1, x1");
}
