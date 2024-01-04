#!/usr/bin/python3
"""pascal triangle alx interview"""


def pascal_triangle(n):
    """function returns list of integers representing the pascal triangle"""
    if (n <= 0):
        return([])
    triangle = []
    for i in range(n):
        row = [1]
        for j in range(1, i):
            val = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(val)
        if (i > 0):
            row.append(1)
        triangle.append(row)
    return (triangle)
