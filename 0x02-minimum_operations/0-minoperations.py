#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """ write a method that calculates number of operations"""
    if not isinstance(n, int) or n < 0 or n == 1:
        return 0
    number = 1
    oper = 0
    i = 0
    while number < n:
        if n % number != 0:
            number += i
            oper += 1
        else:
            i = number
            number += i
            oper += 2
    return (oper if number == n else 0)
