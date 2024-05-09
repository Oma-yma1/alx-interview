#!/usr/bin/python3
"""
island Perimeter project
"""


def island_perimeter(fun):
    """Island Perimenter Function"""
    peri = 0
    for j in range(len(fun)):
        for k in range(len(fun[j])):
            if fun[j][k] == 1:
                peri += 4
                if j > 0 and fun[j-1][k] == 1:
                    peri -= 2
                if k > 0 and fun[j][k-1] == 1:
                    peri -= 2
    return peri
