from typing import List
from functools import reduce

import numpy as np


def evaluate_polynomial(polynomial: List[float], value: float) -> int:
    total = 0
    for power, coefficient in enumerate(polynomial):
        total += coefficient * (value ** power)
    return total


def matrix_method(p1: List[float], p2: List[float]) -> List[float]:
    """
    Take two polynomials of degree n each.
    Evaluate pointwise multiplication x for values -n..n.
    Generate (2n + 1)(2n + 1) Vandermonde matrix A of degree n:
        - Rows involve some fixed value in -n..n exponentiated up by 
          increasing powers in 0..(2n + 1).
        - Columns involve some fixed power in 0..(2n + 1) exponentiating
          increasing bases in -n..n.
    Let c by the coefficient vector of the resulting polynomial.
    Then Ac = x => (A^-1)x = c, which is the desired result.

    Note: in real applications, the matrix and matrix would not be 
          generated during runtime, instead precalculated and stored.
    """

    def generate_vandermonde_matrix(degree: int) -> np.array:
        matrix = [[i ** j for j in range(0, 2 * degree + 1)]
                  for i in range(-degree, degree + 1)]

        return np.array(matrix)

    pointwise_multiplication = []
    
    degree = len(p1) - 1
    for i in range(-degree, degree + 1):
        pointwise_multiplication.append(
                evaluate_polynomial(p1, i) * evaluate_polynomial(p2, i))

    vandermonde_matrix = generate_vandermonde_matrix(degree)
    print(f"Vandermonde matrix: \n{vandermonde_matrix}\n")
    print(f"Polynomial values: \n{np.array(pointwise_multiplication)}\n")

    return np.linalg.inv(vandermonde_matrix).dot(pointwise_multiplication)


def format_polynomial(polynomial: List[float]) -> str:
    polynomial_string = ""

    for power, coefficient in enumerate(polynomial):
        coefficient = int(round(coefficient, 1))
        if coefficient == 1 and power != 0:
            coefficient = ""

        if power == 0:
            polynomial_string += f"{coefficient}"
        elif power == 1:
            polynomial_string += f"{coefficient}x"
        else:
            polynomial_string += f"{coefficient}x^{power}"

        if power != len(polynomial) - 1:
            polynomial_string += " + "

    return polynomial_string


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [1, 1, 1]),
        ([3, 2, 1], [7, 8, 9])
    ]

    for test_case in test_cases:
        polynomial1, polynomial2 = test_case
        print(f"Polynomial 1: {format_polynomial(polynomial1)}")
        print(f"Polynomial 2: {format_polynomial(polynomial2)}\n")
        print(f"""Resulting polynomial: \n"""
              f"""{format_polynomial(matrix_method(polynomial1, polynomial2))}""")
