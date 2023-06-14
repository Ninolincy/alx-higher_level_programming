#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in (matrix):
        newMatrix.append([element * element for element in row])
    return newMatrix
