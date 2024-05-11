void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 0");
    asm("remu x3, x2, x1");
    asm("remu x3, x2, x1");
    asm("remu x3, x2, x1");
    asm("remu x3, x2, x1");
    asm("nop");
    asm("nop");
    asm("nop");
}
