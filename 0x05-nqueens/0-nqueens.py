#!/usr/bin/python3
import sys


def generate_solutions(row, column, queens=[]):
    """
    Generate all possible solutions for the N Queens problem recursively.

    Args:
        row (int): The current row to place the queen.
        column (int): The total number of columns on the chessboard.
        queens (list): The list of queens placed so far.

    Returns:
        list: A list of all possible solutions to the N Queens problem.
    """
    if row == column:
        return [queens]

    solutions = []

    for col in range(column):
        if is_safe(row, col, queens):
            new_queens = queens + [col]
            solutions.extend(generate_solutions(row + 1, column, new_queens))

    return solutions


def is_safe(row, col, queens):
    """
    Check if it is safe to place a queen at the given position.

    Args:
        row (int): The row to place the queen.
        col (int): The column to place the queen.
        queens (list): The list of queens placed so far.

    Returns:
        bool: True if it is safe to place the queen, False otherwise.
    """
    for r, c in enumerate(queens):
        if col == c or abs(row - r) == abs(col - c):
            return False
    return True


def n_queens(n):
    """
    Solve the N Queens problem and return all the solutions.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of all solutions to the N Queens problem.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = generate_solutions(0, n)
    formatted_solutions = []

    for queens in solutions:
        formatted_solution = [[queens.index(col), col] for col in queens]
        formatted_solutions.append(formatted_solution)

    return formatted_solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = n_queens(n)

    for solution in solutions:
        print(solution)
