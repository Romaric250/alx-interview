#!/usr/bin/python3
"""Moving the queen in an NxN chessboard"""

import sys


def place_the_queen(queen, col, prev):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    move_forward = []
    for arr in prev:
        for x in range(col):
            if is_safe(queen, x, arr):
                move_forward.append(arr + [x])
    return move_forward


def get_solutions(row, column):
    sol = [[]]
    for queen in range(row):
        sol = place_the_queen(queen, column, sol)
    return sol


def is_safe(q, x, arr):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    if x in arr:
        return (False)
    else:
        return all(abs(arr[column] - x) != q - column
                   for column in range(q))


def init():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        num = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if num < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (num)


def N_Queens():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    num = init()

    sol = get_solutions(num, num)

    for arr in sol:
        clear = []
        for q, x in enumerate(arr):
            clear.append([q, x])
        print(clear)


if __name__ == '__main__':
    N_Queens()
