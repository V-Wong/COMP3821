from typing import List


def merge_sort(a: List[int]) -> List[int]:
    """
    Divide the array recursively until we reach two subarrays of size 1 or 0.
    Clearly both subarrays are then sorted and we merge in linear time.
    """

    def _merge_sort(a: List[int], low: int, high: int) -> None:
        if low < high:
            mid = (low + high) // 2
            _merge_sort(a, low, mid)
            _merge_sort(a, mid + 1, high)
            _merge(a, low, mid, high)

    def _merge(a: List[int], low: int, mid: int, high: int) -> None:
        copy = [None for _ in a]
        i, j, k = low, mid + 1, 0

        while i < mid + 1 and j <= high:
            if a[i] <= a[j]:
                copy[k] = a[i]
                i += 1
            else:
                copy[k] = a[j]
                j += 1
            k += 1

        while i < mid + 1:
            copy[k] = a[i]
            i += 1
            k += 1

        while j <= high:
            copy[k] = a[j]
            j += 1
            k += 1

        k = 0
        for i in range(low, high + 1):
            a[i] = copy[k]
            k += 1

    _merge_sort(a, 0, len(a) - 1)
    return a


if __name__ == "__main__":
    test_cases = [
        [1, 4, 5, 2, 3, 1, 0, 10],
        list(range(100, 1, -1)),
        [12, 123, 1232, 123232, 111, 111, -3, 123, -3123, 123, 11]
    ]

    for test_case in test_cases:
        print(f"Unsorted: {test_case}")
        assert sorted(test_case) == merge_sort(test_case)
        print(f"Sorted: {test_case}")