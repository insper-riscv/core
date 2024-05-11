void main() __attribute__((noreturn));

void main() {
    asm("mulhu x3, x2, x1");
    asm("mulhu x3, x2, x1");
    asm("mulhu x3, x2, x1");
    asm("mulhu x3, x2, x1");
    asm("nop");
    asm("nop");
    asm("nop");
}
