from typing import List

import math


def minimal_coin_change(denominations: List[int], target: int) -> List[int]:
    """
    Consider the subproblems of summing to i < target.
    Assume we have optimal solutions for all 0..i - 1 < target.
    We can then find the solution for i by considering all 
    previous solutions where adding a single coin attains i.
    This is given by memo[i - denominations[j]] + 1 where 
    j iterates over all denominations.
    We find the minimum of this.

    memo[i] = min{memo[i - denominations[j]] + 1
                  s.t. 0 <= j <= len(denominations)
                  and i - denominations[j] >= 0}
    """
    memo = [0] + [math.inf for _ in range(1, target + 1)]

    for i in range(1, target + 1):
        for j in range(0, len(denominations)):
            cur_min = memo[i - denominations[j]]
            if cur_min + 1 < memo[i]:
                memo[i] = cur_min + 1

    return memo[-1]


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3]
    ]

    for test_case in test_cases:
        print(minimal_coin_change(test_case, 10))