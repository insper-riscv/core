void main() __attribute__((noreturn));

void main() {
    asm("divu x3, x2, x1");
    asm("divu x3, x2, x1");
    asm("divu x3, x2, x1");
    asm("divu x3, x2, x1");
    asm("nop");
    asm("nop");
    asm("nop");
}
