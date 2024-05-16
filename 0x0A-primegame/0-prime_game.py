#!/usr/bin/python3
"""
Module Prime numbers
"""

def is_prime(num):
    """
    return list of prime numbers
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    """
    generate prime
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    """
    return name of the player that won the most rounds
    """
    winners = {'Maria': 0, 'Ben': 0}

    for n in nums:
        primes = generate_primes(n)
        if len(primes) % 2 == 0:
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1

    if winners['Maria'] == winners['Ben']:
        return None
    return max(winners, key=winners.get)

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
