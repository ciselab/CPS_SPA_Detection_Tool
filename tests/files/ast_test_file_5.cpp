// Try-out file

#include <iostream>
#include <unistd.h>

unsigned int microseconds;
unsigned int m = 1000;

int main() {
    microseconds = 5400;
    usleep(microseconds);
    usleep(m);
    return 0;
}
