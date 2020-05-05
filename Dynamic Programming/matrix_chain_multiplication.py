from typing import List

import math


def min_matrix_multiplications(dims: List[int]) -> int:
    """
    We have a memo 2D array where memo[i][j] gives the minimal
    number of multiplications for multiplying matrices i to j.

    We try all subsequences of length 2 up to length n.
    For each length subsequence, we try all possible starting positions.
    We can then calculate the corresponding ending position.
    Then for all possible starting positions, we try all possible cutting positions.

    Recurrence:
        - memo[start][end] = min({memo[start][cut] + memo[cut + 1][end] 
                                 + dims[start - 1] * dims[cut] * dims[end]
                                 for start <= cut <= end - 1})
        - This essentially just tries all cutting positions between start and end.
    """

    n = len(dims)
    memo = [[math.inf for _ in range(n)] for _ in range(n)]
    # 0 multiplications for the diagonal representing 
    # the matrix multiplying with itself.
    for i in range(1, n):
        memo[i][i] = 0

    # For all subsequences of 2 <= length <= n.
    for length in range(2, n + 1):
        # For all possible start indexes.
        for start in range(1, n - length + 1):
            # Calculate the corresponding ending index.
            end = start + length - 1
            # Try every position to cut the sequence.
            for cut in range(start, end):
                cost = memo[start][cut] + memo[cut + 1][end] \
                        + dims[start - 1] * dims[cut] * dims[end]
                memo[start][end] = min(memo[start][end], cost)

    return memo[1][n - 1]


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3]
    ]

    for test_case in test_cases:
        print(min_matrix_multiplications(test_case))