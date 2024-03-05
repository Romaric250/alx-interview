#!/usr/bin/python3
"""
This script calculates the perimeter of an island represented in a 2D grid.
"""

def check_cell(cell_value):
    """
    Check the value of a cell. Returns 1 if the cell is water (0), and 0 if the cell is land (1).
    
    Args:
        cell_value (int): The value of the cell (0 or 1).

    Returns:
        int: 1 if the cell is water, 0 if the cell is land.
    """
    return 1 if cell_value == 0 else 0


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a 2D grid.
    
    Args:
        grid (list of list of int): The 2D grid representing the island. 
                                    1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    assert (1 <= num_rows and num_cols <= 100)
    perimeter = 0
    for row in range(num_rows):
        for col in range(num_cols):
            assert (grid[row][col] == 0) or (grid[row][col] == 1)
            if grid[row][col] == 1:
                if row-1 < 0:
                    perimeter += 1
                else:
                    perimeter += check_cell(grid[row-1][col])
                if col-1 < 0:
                    perimeter += 1
                else:
                    perimeter += check_cell(grid[row][col-1])

                try:
                    perimeter += check_cell(grid[row+1][col])
                except IndexError:
                    perimeter += 1
                try:
                    perimeter += check_cell(grid[row][col+1])
                except IndexError:
                    perimeter += 1

    return perimeter