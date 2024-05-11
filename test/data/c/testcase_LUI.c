void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 0");
    asm("lui x8, 1");
    asm("lui x8, 1");
    asm("lui x8, 1");
    asm("lui x8, 1");
    asm("nop");
    asm("nop");
    asm("nop");
}
