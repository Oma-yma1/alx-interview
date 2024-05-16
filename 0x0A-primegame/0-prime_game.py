#!/usr/bin/python3
"""
Prime Game Module
"""


def sieve(n):
    """Generate a list of primes up to n using Sieve of Eratosthenes"""
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def calculate_moves(n, primes):
    """Calculate number of moves possible with given primes"""
    marked = [False] * (n + 1)
    moves = 0
    for prime in primes:
        if prime > n:
            break
        if not marked[prime]:
            moves += 1
            for multiple in range(prime, n + 1, prime):
                marked[multiple] = True
    return moves


def isWinner(x, nums):
    """
    Determine the winner of the game
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve(max_num)

    winners = {'Maria': 0, 'Ben': 0}

    for n in nums:
        moves = calculate_moves(n, primes)
        if moves % 2 == 0:
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1

    if winners['Maria'] > winners['Ben']:
        return 'Maria'
    elif winners['Ben'] > winners['Maria']:
        return 'Ben'
    else:
        return None
