"""
Computer the square root of a number (use a function with loop).
1. The input is a number, or enter/return to halt process.
2. The outputs are the program's estimate of the square root using
Newton's method of successive approximations, and Python's own estimate
using math.sqrr
"""


import math

TOLERANCE = .000001

def newton(x):
    """Returns the square root of x."""
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    return estimate

def main():
    """Allows the user to obtain square roots."""
    while True:
        # Recevie the input number from the user
        x = input("Enter a positive number or enter/return to quit:")
        if x == "":
            break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))


if __name__ == "__main__":
    main()
