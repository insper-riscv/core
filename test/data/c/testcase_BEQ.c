void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0, 0");
    asm("beq  x1, x0, j_eq");
    asm("addi x0, x0,  0");
    asm("addi x3, x0,  8");
    asm("addi x3, x0,  4");
    asm("j_eq:");
    asm("addi x3, x0,  2");
    asm("addi x3, x0,  1");
    asm("nop");
    asm("nop");
    asm("nop");
}
