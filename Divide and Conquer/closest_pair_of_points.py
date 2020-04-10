from typing import List, Tuple
import math


def calculate_distance(p0: Tuple[int, int], p1: Tuple[int, int]) -> int:
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


def brute_force_find_closest_pair(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    min_distance = math.inf
    closest_pair = None

    for i0, p0 in enumerate(points):
        for p1 in points[i0 + 1::]:
            if calculate_distance(p0, p1) < min_distance:
                min_distance = calculate_distance(p0, p1)
                closest_pair = p0, p1

    return closest_pair


def find_closest_pair(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    We sort our points to form two lists:
        - sorted_x: sorted by x coordinates.
        - sorted_y: sorted by y coordinates.
    We half these two lists to form:
        - left_x: lower half of sorted_x.
        - right_x upper half of sorted_x.
        - and similarly for y.
    We then call our functions recursively to find:
        - l0, l1: closest set of points on left half.
        - r0, r1: closest set of points on right half.
    We then find the closest set of points in the crossover:
        - min_half_distance = min(d(l0, l1), d(r0, r1)).
        - max_x_coordinate = largest x coordinate in left_x.
        - If there exists points q, r such that d(q, r) < min_half_distance, then:
            - Each of q and r have x coordinate within min_half_distance of max_x_coordinate.
        - We hence construct S_y: points within min_half_distance of max_x_coordinate, sorted by y coordinates.
        - Now, if there exists points s, s' such that d(s, s') < min_half_distance, then:
            - s and s' are within 15 positions of each other in the sorted list S_y.
            - We hence only need to compare each point in S_y with the next 15 points. 
    """

    def _helper(sorted_x: List[Tuple[int, int]],
                sorted_y: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if len(sorted_x) <= 3:
            return brute_force_find_closest_pair(sorted_x)

        left_x = sorted_x[0:len(sorted_x) // 2]
        right_x = sorted_x[len(sorted_x) // 2::]
        left_y = sorted_y[0:len(sorted_y) // 2]
        right_y = sorted_y[len(sorted_y) // 2::]

        l0, l1 = _helper(left_x, left_y)
        r0, r1 = _helper(right_x, right_y)

        min_half_distance = min(calculate_distance(l0, l1),
                                calculate_distance(r0, r1))
        max_x_coordinate = max(p[0] for p in left_x)
        S = [p for p in sorted_x if 
             abs(p[0] - max_x_coordinate) <= min_half_distance]
        S_y = [p for p in S if p in sorted_y]

        closest_crossover_pair = None
        min_crossover_distance = math.inf
        for i, s0 in enumerate(S_y):
            # Note that this loop runs in O(1) time.
            for s1 in S_y[i + 1:i + 16]:
                cur_distance = calculate_distance(s0, s1)
                if cur_distance < min_crossover_distance:
                    min_crossover_distance = cur_distance
                    closest_crossover_pair = s0, s1

        if min_crossover_distance < min_half_distance:
            return closest_crossover_pair
        elif calculate_distance(l0, l1) < calculate_distance(r0, r1):
            return l0, l1
        else:
            return r0, r1

    sorted_x = sorted(points, key=lambda p: p[0])
    sorted_y = sorted(points, key=lambda p: p[1])

    return _helper(sorted_x, sorted_y)

    
if __name__ == "__main__":
    test_cases = [
        [[(5.5, 5.5), (2, 3), (3, 4), (1, 2), (5, 5),
          (0, 0), (1, 1), (0, 1), (0, 1.1), (1, 2.05)], (1, 2), (1, 2.05), (0, 0)]
    ]
    
    for test_case in test_cases:
        points = test_case[0]
        closest_pair = test_case[1], test_case[2]
        assert find_closest_pair(points) == closest_pair
