void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 0");
    asm("addi x1, x0, 7");
    asm("andi x2, x1, 6");
    asm("andi x2, x1, 5");
    asm("addi x0, x0, 0");
    asm("andi x2, x1, 7");
    asm("nop");
    asm("nop");
    asm("nop");
}
