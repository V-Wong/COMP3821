from typing import List
import math
import cmath


def nth_primitive_root_of_unity(n: int) -> complex:
    return cmath.rect(1, 2 * math.pi / n)


def simple_dft(a: List[int]) -> List[complex]:
    n = len(a)
    A = [0 for _ in range(n)]

    w = 1
    for i in range(n):
        total = 0
        for j in range(n):
            total += a[j] * (w ** j)
        w *= nth_primitive_root_of_unity(n)
        A[i] = total

    return A


def fft(a: List[int]) -> List[complex]:
    n = len(a)
    if n == 1:
        return a
    else:
        a_even, a_odd = a[0::2], a[1::2]
        y_even, y_odd = fft(a_even), fft(a_odd)
        A = [0 for _ in range(n)]
        w = 1
        for k in range(n // 2):
            A[k] = y_even[k] + w * y_odd[k]
            A[n // 2 + k] = y_even[k] - w * y_odd[k]
            w = w * nth_primitive_root_of_unity(n)
    return A


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    A = [(round(z.real, 1), round(z.imag, 1)) for z in simple_dft(a)]
    print(A)