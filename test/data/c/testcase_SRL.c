void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 256");
    asm("addi x2, x0,   6");
    asm("srl  x3, x1,  x2");
    asm("addi x0, x0,   0");
    asm("addi x0, x0,   0");
    asm("srl  x3, x1,  x2");
    asm("srl  x3, x1,  x2");
    asm("srl  x3, x1,  x2");
    asm("nop");
    asm("nop");
    asm("nop");
}
