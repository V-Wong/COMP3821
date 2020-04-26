from typing import List


def longest_increasing_subsequence(sequence: List[int]) -> List[int]:
    """
    We have a len_memo array that stores the length of the longest
    increasing subsequence at any given index i.

    Base case: length 1 sequence is clearly increasing.
    
    Optimal substructure: if we know all the longest increasing subsequences
    ending at index i for a sequence of length n. Then the longest increasing
    subsequence of a sequence of length n + 1, can be found by possibly
    extending any of these longest subsequences at some index i.

    To solve lis(n + 1):
        - We look through len_memo[0..n] to find the largest value
          at index i where sequence[i] < sequence[n + 1].
        - We are essentially trying to extend the longest subsequence
          obtained in lis(n) with element lis(n + 1) if possible.
        - We then set len_memo to be the increment of len_memo[i].

    Optimality argument (cut and paste):
        - Where 0 <= i <= k and 0 <= m < i.
        - Truncating optimal solution for lis(i) must produce 
          optimal solution for subproblem lis(m).
        - Otherwise we could find better solution for lis(i)
          by extending such better solution of lis(m).
    """

    def helper(sequence: List[int], i: int, 
               len_memo: List[int], index_memo) -> List[int]:
        if i < len(sequence):
            prev_longest = max([l for m, l in enumerate(len_memo[:i])
                                if sequence[m] < sequence[i]], default=None)
            
            prev_longest_index = -1
            if prev_longest:
                for index, num in enumerate(len_memo[:i]):
                    if num == prev_longest and num < sequence[i]:
                        prev_longest_index = index

            if prev_longest_index >= 0:
                len_memo[i] = len_memo[prev_longest_index] + 1
                index_memo[i] = prev_longest_index
                
            return helper(sequence, i + 1, len_memo, index_memo)
    
    def reconstruct_subsequence(sequence: List[int],
                                index_memo: List[int]) -> List[int]:
        reconstruction = []

        cur_index = max(index_memo)
        reconstruction.insert(0, sequence[index_memo.index(cur_index)])
        while cur_index >= 0:
            reconstruction.insert(0, sequence[cur_index])
            cur_index = index_memo[cur_index]

        return reconstruction
            
    len_memo = [1 for _ in sequence]
    index_memo = [-1 for i, _ in enumerate(sequence)]
    helper(sequence, 0, len_memo, index_memo)
    return reconstruct_subsequence(sequence, index_memo)


if __name__ == "__main__":
    test_cases = [
        list(range(10, 0, -1)),
        list(range(0, 10, 1)) + [0, 10, 11],
        [3, 1, 2, 3, 2, 5, 1, 1, 6, 0, 7],
        [10, 22, 9, 33, 21, 50, 41, 60] 
    ]

    for test_case in test_cases:
        print(longest_increasing_subsequence(test_case))
