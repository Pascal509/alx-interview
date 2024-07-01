#!/usr/bin/python3
"""
This module returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers of Pascal's triangle.

    Parameters:
    n (int): lists of Pascal's triangle

    Returns:
    int: list of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle
