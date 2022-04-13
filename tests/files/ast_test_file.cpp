// Try-out file

#include <iostream>
#include <unistd.h>

unsigned int microseconds;

int main() {
    std::cout << "Hello World!" << std::endl;
    microseconds = 5400;
    usleep(microseconds);
    something_else();
    return 0;
}

void something_else() {
    std::cout << "FOOBAR" << std::endl;
    usleep(4200);
}
