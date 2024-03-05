#!/usr/bin/env python
import time

HC_SOMETHING = 9000
time.sleep(2)


def not_being_used():
    unused_var = 404


class SmallClass:
    in_class_outside_method = 600

    @classmethod
    def check(cls, node):
        print("hello")
        if "print" in node:
            world = 42
            return world
        return None

    def other_check(self, node):
        print("nothing")
        nothing = 0
        return nothing


def tenthousendmilesundersea():
    deep = 3.14
    time.sleep(256)
    # old_new = HC_SOMETHING


def going_to_earths_core():
    bar = 4.13
    time.sleep(128)
    tenthousendmilesundersea()


def something():
    print("Lorem")
    print("hard coded")
    foo = 5.3
    time.sleep(64)
    going_to_earths_core()


def print_numbers():
    time.sleep(32)
    ipsum = 42
    print(ipsum)


def main():
    valuable_number = 42
    print("Hello, World!")
    time.sleep(2)
    something()
    print_numbers()
    same_val = HC_SOMETHING


random_in_between = 400
time.sleep(4)


if __name__ == "__main__":
    random = 303
    time.sleep(5)
    main()
