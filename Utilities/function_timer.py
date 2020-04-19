from typing import Callable

from time import clock


def timer(f: Callable, *args) -> (float, ):
    starting_time = clock()
    calculated_value = f(*args)
    ending_time = clock()

    return ending_time - starting_time, calculated_value


def pretty_timer(f: Callable, *args) -> str:
    time, calculated_value = timer(f, *args)
    return f"Time: {time}. Calculated value: {calculated_value}"