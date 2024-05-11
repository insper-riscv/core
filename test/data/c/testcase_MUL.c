void main() __attribute__((noreturn));

void main() {
    asm("mul x3, x2, x1");
    asm("mul x3, x2, x1");
    asm("mul x3, x2, x1");
    asm("mul x3, x2, x1");
    asm("nop");
    asm("nop");
    asm("nop");
}
