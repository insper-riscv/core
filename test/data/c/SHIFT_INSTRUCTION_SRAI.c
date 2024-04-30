void main() __attribute__((noreturn));

void main() {
    asm("addi x1, x0,    256");
    asm("srai x2, x1,      6");
    asm("srai x2, x1,      6");
    asm("lui  x8,          1");
    asm("srai x2, x8,      6");
    asm("srai x2, x8,      6");
    asm("lui  x9,     524288");
    asm("srai x3, x9,      6");
    asm("srai x3, x9,      6");
    asm("srai x2, x1,      6");
    asm("srai x2, x8,      6");
    asm("srai x3, x9,      6");
}
