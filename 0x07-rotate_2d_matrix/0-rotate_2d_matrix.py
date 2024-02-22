#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    """
    n = len(matrix[0])

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]