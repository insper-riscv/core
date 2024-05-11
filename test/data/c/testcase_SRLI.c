void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 256");
    asm("srli x2, x1,   6");
    asm("srli x2, x1,   6");
    asm("addi x0, x0,   0");
    asm("srli x2, x1,   6");
    asm("srli x2, x1,   6");
    asm("nop");
    asm("nop");
    asm("nop");
}
