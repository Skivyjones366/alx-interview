#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    return None


def rm_multiples(ls, x):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        ls (list of int): An array of possible prime numbers.
        x (int): The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    # This loop iterates over multiples of a prime number and marks them as
    # non-prime by setting their corresponding value to 0 in the input
    # list ls. Starting from 2, it sets every multiple of x up to the
    # length of ls to 0. If the index i * x is out of range for the list ls,
    # the try block will raise an IndexError exception, and the loop will
    # terminate using the break statement.
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
