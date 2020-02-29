from typing import List

"""
The sequence of values A[1], A[2], . . . , A[n] is unimodal: 
For some index p between 1 and n, the values in the array entries increase 
up to position p in A and then decrease the remainder of the way until position n.

Find the index of the peak entry in O(log(n)) time.
"""


def peak_finder(array: List[int]):
    def _binary_search(array: List[int], low: int, high: int) -> int:
        if low >= high:
            return None
        else:
            mid = (low + high) // 2
            
            if array[mid - 1] < array[mid] > array[mid + 1]:
                return mid
            elif array[mid - 1] < array[mid] < array[mid + 1]:
                return _binary_search(array, mid + 1, high)
            else:
                return _binary_search(array, low, mid)

    return _binary_search(array, 0, len(array) - 1)


if __name__ == "__main__":
    test_cases = [
            ([1, 2, 3, 2, 1], 2),
            ([1], None),
            ([1, 2], None),
            ([1, 2, 1], 1),
            ([1, 2, 3, 4, 5, 6, 7, 8], None),
            ([1, 2, 3, 4, 5, 6, 7, 8, 7], 7),
            ([1, 2, 0, 0, 0, 0, 0, 0], 1),
            ([], None)
    ]

    for test_case in test_cases:
        array, peak = test_case
        assert peak_finder(array) == peak