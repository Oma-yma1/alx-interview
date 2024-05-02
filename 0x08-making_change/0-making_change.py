#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the few number of coins needed to meet a given amount total
    """
    if total < 1:
        return 0
    coins.sort(reverse=True)
    result = 0
    for coin in coins:
        if total <= 0:
            break
        result += total // coin
        total %= coin
    return result if total == 0 else -1
