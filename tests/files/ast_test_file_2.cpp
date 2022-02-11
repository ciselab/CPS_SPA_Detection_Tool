// Try-out file

#include <iostream>
#include <unistd.h>

unsigned int microseconds;

int main() {
    std::cout << "Hello World!" << std::endl;
    microseconds = 5400;
    usleep(microseconds);
    something_else();
    something_completely_different();
    return 0;
}

void something_else() {
    std::cout << "FOOBAR" << std::endl;
    usleep(50000);
}

void something_completely_different() {
    std::cout << "FOODBAR" << std::endl;
    usleep(3);
}
