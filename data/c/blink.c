#include "base.h"

void main() {
    while (1) {
        sleep(50000000);
        digitalWrite(LEDR, 1);
        sleep(50000000);
        digitalWrite(LEDR, 0);
    }
}
