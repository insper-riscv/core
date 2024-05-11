void main() __attribute__((noreturn));

void main() {
    asm("mulhsu x3, x2, x1");
    asm("mulhsu x3, x2, x1");
    asm("mulhsu x3, x2, x1");
    asm("mulhsu x3, x2, x1");
    asm("nop");
    asm("nop");
    asm("nop");
}
