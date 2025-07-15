#!/usr/bin/python3
"""
A simple script to calculate the factorial of a given number
provided via command-line arguments.
"""

import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.
    
    Args:
        n (int): A non-negative integer.

    Returns:
        int: Factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <non-negative integer>")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Negative number provided.")
        result = factorial(number)
        print(f"Factorial of {number} is {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)
