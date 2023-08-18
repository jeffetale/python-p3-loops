#!/usr/bin/env python3


def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
    # code goes here!
    pass


def square_integers(int_list):
    return [num**2 for num in int_list]

    # code goes here!
    pass


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    # code goes here!
    pass


happy_new_year()
