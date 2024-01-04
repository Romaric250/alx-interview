#!/usr/bin/python3
"""A script to get pascals triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.

    Args:
        n (int): The height of the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        temp_list = []

        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        triangle.append(temp_list)

    return triangle