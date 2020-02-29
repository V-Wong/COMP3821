from typing import List

"""
Suppose we have 2 sorted arrays of length n.
Find the median of the two combined arrays.
Solution should run in O(log(n)) time.
"""


def find_median_of_two_arrays(array1: List[int], array2: List[int], 
                              size: int) -> float:
    """
    Suppose m1 and m2 are the medians of array1 and array2 respectively.
    Then the overall median m must lie in [m1, m2].
    We perform a modified binary search to progressively tighten this interval
    until we reach a single element list.
    """

    if size <= 0:
        return None
    elif size == 1:
        return min(array1[0], array2[0])
    else:
        m1, m2 = array1[size // 2], array2[size // 2]

        if m1 == m2:
            return m1
        elif m1 < m2:
            return find_median_of_two_arrays(array1[size // 2:], 
                                             array2[:size // 2 + 1], 
                                             size - size // 2)
        else:
            return find_median_of_two_arrays(array1[:size // 2 + 1], 
                                             array2[size // 2:], 
                                             size - size // 2)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [4, 5, 6], 3),
        ([1, 3, 5, 7], [2, 4, 6, 8], 4),
        ([2, 4, 6], [1, 3, 5], 3),
        (list(range(10, 20 + 1)), list(range(10 + 1)), 10),
        ([2, 4, 6, 8, 10, 12, 14], [7, 9, 11, 13, 15, 17, 19], 10)
    ]

    for test_case in test_cases:
        array1, array2, median = test_case
        assert find_median_of_two_arrays(array1, array2, len(array1)) == median