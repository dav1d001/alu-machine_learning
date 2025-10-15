#!/usr/bin/env python3
""" A function that calculates
 the shape of a matrix
 using recursion
 """


def matrix_shape(matrix):
    """
    It calculates the shape of a matrix
    """
    shape = []
    while type(matrix) == list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
