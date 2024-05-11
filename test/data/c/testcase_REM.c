void main() __attribute__((noreturn));

void main() {
    asm("rem x3, x2, x1");
    asm("rem x3, x2, x1");
    asm("rem x3, x2, x1");
    asm("rem x3, x2, x1");
    asm("nop");
    asm("nop");
    asm("nop");
}
