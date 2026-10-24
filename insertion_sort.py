def insertion_sort_decreasing(arr):
    """Sort a list in place into monotonically decreasing order.

    Follows the INSERTION-SORT procedure from CLRS (Chapter 2), with the
    comparison reversed so larger elements come first.

    Args:
        arr: A list of mutually comparable items.

    Returns:
        The same list, sorted from largest to smallest.

    Time complexity: O(n^2) worst case, O(n) best case (already sorted
    in decreasing order). Space complexity: O(1).
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # Shift elements smaller than key one position to the right
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


if __name__ == "__main__":
    examples = [
        [5, 2, 4, 6, 1, 3],
        [],
        [7],
        [1, 2, 3, 4, 5],
        [9, 8, 7, 6],
        [3, 3, 1, 2, 2],
        [-4, 10, 0, -1, 5],
    ]
    for data in examples:
        original = list(data)
        print(f"{original} -> {insertion_sort_decreasing(data)}")