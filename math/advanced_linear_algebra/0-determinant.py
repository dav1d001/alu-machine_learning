#!/usr/bin/env python3
"""
Module that contains a function to calculate the determinant of a matrix.
"""


def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): The matrix whose determinant should be calculated.

    Returns:
        int or float: The determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.
    """
    # Validate matrix type
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Handle empty matrix case
    if matrix == []:
        raise TypeError("matrix must be a list of lists")

    # Handle 0x0 matrix
    if matrix == [[]]:
        return 1

    # Check for square matrix
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case using Laplace expansion
    det = 0
    for c in range(n):
        sub_matrix = [row[:c] + row[c + 1:] for row in matrix[1:]]
        sign = (-1) ** c
        det += sign * matrix[0][c] * determinant(sub_matrix)
    return det

