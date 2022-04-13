#include <iostream>
#include <unistd.h>

unsigned int microseconds;

int main(int argc, char** argv) {
    determine_sleep_time();
    usleep(microseconds);
    int ere_sting_var = 42.4;
    usleep(4200);
    return 0;
}

void determine_sleep_time() {
    microseconds = 5000;
}