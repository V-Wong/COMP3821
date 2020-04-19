from typing import Dict

import sys
import os
sys.path.append("../Utilities")

from function_timer import pretty_timer


def naive_method(n: int) -> int:
    def fib(n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return fib(n)


def memoization_method(n: int) -> int:
    def fib(n: int, cache: Dict[int, int]={0: 1, 1: 1}) -> int:
        if n in cache:
            return cache[n]
        else:
            cache[n] = res = fib(n - 1) + fib(n - 2)
            return res

    return fib(n)


def bottom_up_method(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    print(pretty_timer(naive_method, 35))
    print(pretty_timer(memoization_method, 35))
    print(pretty_timer(bottom_up_method, 35))