from typing import List


class InversionCounter:
    @staticmethod
    def calculate(a: List[int], b: List[int]) -> int:
        return InversionCounter._merge_sort(a, 0, len(a) - 1)

    @staticmethod
    def _merge_sort(a: List[int], low: int, high: int) -> int:
        inversion_count = 0
        if low < high:
            mid = (low + high) // 2
            inversion_count += InversionCounter._merge_sort(a, low, mid)
            inversion_count += InversionCounter._merge_sort(a, mid + 1, high)
            inversion_count += InversionCounter._merge(a, low, mid, high)
        return inversion_count

    @staticmethod
    def _merge(a: List[int], low: int, mid: int, high: int) -> int:
        """
        Uses the same concept as the regular inversion counter.
        But we first do a pass to count all significant inversions.
        Then we perform another pass for the merge.

        Note: We cannot combine the two passes into one.
        Suppose: a[i] > a[j] but not a[i] > 2 * a[j], and a[i + 1] > 2 * a[j].
        Then a[j] becomes the next element in our merged array and we incremet j++.
        But then we just missed counting the significant inversion a[i + 1] > 2 * a[j].
        """

        inversion_count = 0
        temp = []

        i, j = low, mid + 1

        while i <= mid and j <= high:
            if a[i] > 2 * a[j]:
                inversion_count += mid - i + 1
                j += 1
            else:
                i += 1

        i, j = low, mid + 1

        while i <= mid and j <= high:
            if a[i] < a[j]:
                temp.append(a[i])
                i += 1
            else:
                temp.append(a[j])
                j += 1

        while i <= mid:
            temp.append(a[i])
            i += 1

        while j <= high:
            temp.append(a[j])
            j += 1

        i, k = low, 0
        while i <= high:
            a[i] = temp[k]
            i, k = i + 1, k + 1

        return inversion_count


if __name__ == "__main__":
    test_cases = [
        [[i for i in range(12)],
         [0, 10, 8, 11, 6, 9, 2, 3, 5, 7, 1, 4]],
        [[0, 1, 2, 3, 4],
         [1, 20, 6, 4, 5]]
    ]

    for test_case in test_cases:
        print("b:", test_case[0])
        print("a:", test_case[1])
        print("Inversion count:",
              InversionCounter.calculate(test_case[1], test_case[0]))
