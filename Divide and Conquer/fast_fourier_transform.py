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


def fft(a: List[complex]) -> List[complex]:
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


def ifft(A: List[complex]) -> List[complex]:
    def _ifft(A: List[complex]) -> List[complex]:
        n = len(A)
        if n == 1:
            return A
        else:
            A_even, A_odd = A[0::2], A[1::2]
            y_even, y_odd = _ifft(A_even), _ifft(A_odd)
            a = [0 for _ in range(n)]
            w = 1
            for k in range(n // 2):
                a[k] = y_even[k] + w * y_odd[k]
                a[n // 2 + k] = y_even[k] - w * y_odd[k]
                w = w * nth_primitive_root_of_unity(-n)
            return a
    return _ifft([a / len(A) for a in A])


if __name__ == "__main__":
    sequence = [1, 2, 3, 4]
    print([(round(z.real, 2), round(z.imag, 2)) for z in fft(sequence)])
    print([(round(z.real, 2), round(z.imag, 2)) for z in ifft(fft(sequence))])