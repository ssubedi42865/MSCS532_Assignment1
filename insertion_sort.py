def insertion_sort_descending(numbers):
    """Sort numbers from largest to smallest."""
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        # Shift smaller numbers one position to the right.
        while j >= 0 and numbers[j] < key:
            numbers[j + 1] = numbers[j]
            j -= 1

        # Insert the current number in its correct position.
        numbers[j + 1] = key

    return numbers


if __name__ == "__main__":
    values = [12, 5, 23, 7, 23, 1, 18]

    print("Original array:", values)
    insertion_sort_descending(values)
    print("Sorted array:", values)