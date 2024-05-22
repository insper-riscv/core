#ifndef __BASE_H__
#define __BASE_H__

#define LEDR                        128
#define sleep(cycles)               for (long i = 0; i < (cycles / 2); i++) asm("");
#define digitalWrite(pin, value)    (*((volatile int *)pin) = value)


void main() __attribute__((noreturn));

#endif
