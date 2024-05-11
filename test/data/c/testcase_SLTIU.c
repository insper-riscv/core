void main() __attribute__((noreturn));

void main() {
    asm("lui   x10,      524288");
    asm("addi   x1,  x0,      8");
    asm("sltiu  x2,  x1,      7");
    asm("sltiu  x2,  x1,      9");
    asm("lui    x9,      262144");
    asm("sltiu  x2,  x1,      4");
    asm("sltiu  x2,  x1,     10");
    asm("sltiu  x2,  x1,     40");
    asm("sltiu  x2,  x9,      1");
    asm("sltiu  x2, x10,      1");
    asm("nop");
    asm("nop");
    asm("nop");
}
