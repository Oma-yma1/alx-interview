#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    k = len(matrix)
    for i in range(k):
        for j in range(i + 1, k):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(k):
        matrix[i].reverse()
