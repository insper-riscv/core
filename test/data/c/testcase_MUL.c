void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 0");
    asm("mul x3, x2, x1");
    asm("mul x3, x2, x1");
    asm("mul x3, x2, x1");
    asm("mul x3, x2, x1");
    asm("nop");
    asm("nop");
    asm("nop");
}
