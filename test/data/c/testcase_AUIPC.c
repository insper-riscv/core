void main() __attribute__((noreturn));

void main() {
    asm("auipc x8, 1");
    asm("auipc x8, 1");
    asm("auipc x8, 1");
    asm("auipc x8, 1");
}
