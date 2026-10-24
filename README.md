# MSCS532_Assignment1

Python implementation of Insertion Sort (CLRS, Chapter 2) that sorts an array
into **monotonically decreasing** order.

## Run

    python3 insertion_sort.py

## Algorithm

For each element `key` at index `j`, shift every earlier element that is
*smaller* than `key` one position to the right, then insert `key` into the gap.
The only change from the textbook version is the comparison (`<` instead of `>`).

- Worst case: O(n^2), best case: O(n), space: O(1), in-place and stable.
