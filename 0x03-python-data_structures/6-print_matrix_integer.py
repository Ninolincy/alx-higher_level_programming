#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for s in matrix:
        for t in s:
            if t != s[-1]:
                print("{:d}".format(t), end=" ")
            else:
                print("{:d}".format(t), end="")
        print()
