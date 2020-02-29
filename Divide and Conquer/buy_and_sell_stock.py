from typing import List, Tuple

"""
Suppose p(i) gives the price of stocks on day i.
Find the indexes i, j, with j > i such that p(j) - p(i) is a maximum.
Solution should run in O(nlog(n)) time.
"""


def find_max_profit(prices: List[int]) -> Tuple[int, int, int]:
    """
    We can divide an array of length 2 into two subarrays of length n / 2.
    Then the optimal purchasing strategy is one of 3 cases:
        - Buy and sell in the left subarray.
        - Buy and sell in the right subarray.
        - Buy in the left subarray, and sell in the right subarray.
    The first two scenarios are produced by the recursion.
    The last scenario we must calculate manually.
    We take the best of the three, and merge up our solution.
    """

    def _helper(prices: int, low: int, high: int) -> Tuple[int, int, int]:
        if low >= high:
            return 0, None, None
        
        mid = (low + high) // 2

        left_profit, left_buy, left_sell = _helper(prices, low, mid)
        right_profit, right_buy, right_sell = _helper(prices, mid + 1, high)
        
        min_left = min(prices[low:mid + 1])
        max_right = max(prices[mid + 1:high + 1])
        crossover_profit = max_right - min_left
            
        max_profit = max(left_profit, right_profit, crossover_profit)

        if max_profit == left_profit:
            return max_profit, left_buy, left_sell
        elif max_profit == right_profit:
            return max_profit, right_buy, right_sell
        else:                
            return max_profit, \
                   prices[low:high + 1].index(min_left), \
                   prices[mid + 1:high + 1].index(max_right) + (mid + 1)

    return _helper(prices, 0, len(prices) - 1)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 3, 0, 3),
        ([5, 4, 3, 2], 0, None, None),
        ([], 0, None, None),
        ([1], 0, None, None),
        (list(range(100 + 1)), 100, 0, 100),
        (list(range(100 + 1)) + list(range(50, 0 - 1, -1)), 100, 0, 100)
    ]

    for test_case in test_cases:
        prices, max_profit, buy_time, sell_time = test_case
        assert find_max_profit(prices) == (max_profit, buy_time, sell_time)
