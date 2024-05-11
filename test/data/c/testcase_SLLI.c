void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 8");
    asm("slli x2, x1, 4");
    asm("slli x2, x1, 4");
    asm("addi x0, x0, 0");
    asm("slli x2, x1, 4");
    asm("nop");
    asm("nop");
    asm("nop");
}
