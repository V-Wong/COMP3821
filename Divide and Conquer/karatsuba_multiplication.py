import math

# To prevent exceeding maximum recusion depth.
CUTOFF = 64


def get_num_digits(num: int, base: int) -> int:
    if num == 0:
        return 0
    else:
        return math.ceil(math.log(num, base))


def karatsuba(a: int, b: int, base: int) -> int:
    if get_num_digits(a, base) <= CUTOFF or get_num_digits(b, base) <= CUTOFF:
        return a * b
    else:
        num_digits = max(get_num_digits(a, base), get_num_digits(b, base))

        a_1 = a // base ** (num_digits // 2)
        a_0 = a % base ** (num_digits // 2)
        b_1 = b // base ** (num_digits // 2)
        b_0 = b % base ** (num_digits // 2)

        x = karatsuba(a_0, b_0, base)
        y = karatsuba(a_0, b_1, base)
        z = karatsuba(a_1, b_0, base)
        w = karatsuba(a_1, b_1, base)

        return w * (base ** num_digits) + (y + z) * (base ** (num_digits // 2)) + x


if __name__ == "__main__":
    test_cases = [
            (1, 2, 10),
            (1, 2, 5),
            (5, 6, 4),
            (5, 6, 3),
            (55, 50, 2),
            (123456789, 987654321, 2)
    ]

    for test_case in test_cases:
        a, b, base = test_case
        assert karatsuba(a, b, base) == a * b
