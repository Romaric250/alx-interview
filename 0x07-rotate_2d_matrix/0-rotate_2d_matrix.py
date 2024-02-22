#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            # Transpose the matrix
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # Reverse each row
        matrix[i] = matrix[i][::-1]

    return matrix