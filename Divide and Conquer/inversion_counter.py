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
        inversion_count = 0
        temp = []

        i, j = low, mid + 1
        while i <= mid and j <= high:
            if a[i] < a[j]:
                temp.append(a[i])
                i += 1
            else:
                inversion_count += mid - i + 1
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


class BruteForceInversionCounter:
    @staticmethod
    def calculate(a: List[int], b: List[int]) -> int:
        inversion_count = 0
        inversion_table = BruteForceInversionCounter.gen_inversion_table(a, b)

        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if inversion_table[i] > inversion_table[j]:
                    inversion_count += 1

        return inversion_count
  
    @staticmethod
    def gen_inversion_table(a: List[int], b: List[int]) -> int:
        """
        inversion_table[i] gives the index for
        the ith element in array b in array a.

        Note: assume b is list of consecutive increasing naturals
        and that len(a) == len(b).
        """

        inversion_table = [-1 for _ in range(len(a))]

        for i in b:
            inversion_table[i] = a.index(i)

        return inversion_table


if __name__ == "__main__":
    test_cases = [
        [[i for i in range(12)],
         [0, 10, 8, 11, 6, 9, 2, 3, 5, 7, 1, 4]]
    ]

    for test_case in test_cases:
        print("b:", test_case[0])
        print("a:", test_case[1])
        print("Inversion count (brute force):",
              BruteForceInversionCounter.calculate(test_case[1], test_case[0]))
        print("Inversion count (modified merge sort):",
              InversionCounter.calculate(test_case[1], test_case[0]))
