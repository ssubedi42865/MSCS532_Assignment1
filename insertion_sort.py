"""Insertion Sort in monotonically decreasing order.

Based on INSERTION-SORT from Chapter 2 of Cormen, Leiserson, Rivest, & Stein
(2022), Introduction to Algorithms (4th ed.), modified to sort from largest
to smallest.
"""

import random


def insertion_sort_decreasing(arr):
    """Sort a list in place into monotonically decreasing order.

    Args:
        arr: A list of mutually comparable items.

    Returns:
        The same list, sorted from largest to smallest.

    Time complexity: O(n^2) worst case, O(n) best case.
    Space complexity: O(1) extra space.
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # Loop invariant: arr[0..j-1] is sorted in decreasing order.
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def run_tests():
    """Verify the sort against Python's built-in sorted() on many inputs."""
    fixed_cases = [
        [],
        [7],
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4, 5],
        [9, 8, 7, 6],
        [3, 3, 1, 2, 2],
        [-4, 10, 0, -1, 5],
        [2.5, -1.5, 3.0, 0.0],
    ]
    for case in fixed_cases:
        expected = sorted(case, reverse=True)
        assert insertion_sort_decreasing(list(case)) == expected, case

    random.seed(42)
    for _ in range(500):
        case = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        expected = sorted(case, reverse=True)
        assert insertion_sort_decreasing(list(case)) == expected, case

    print("All tests passed.")


def main():
    data = [31, 41, 59, 26, 41, 58]
    print("Before:", data)
    print("After: ", insertion_sort_decreasing(data))
    print()
    run_tests()


if __name__ == "__main__":
    main()
