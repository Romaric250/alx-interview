#!/usr/bin/python3
def switch_rows_and_columns(mat, size):
    for x in range(size):
        for y in range(x, size):
            mat[x][y], mat[y][x] = mat[y][x], mat[x][y]

def flip_rows(mat):
    for row in mat:
        row.reverse()

def rotate_2d_matrix(mat):
    size_of_matrix = len(mat)

    switch_rows_and_columns(mat, size_of_matrix)
    flip_rows(mat)

    return mat