from utils import merge


def insertion_sort(a):
    """Sort list of items in increasing order
    example: A = [5,2,4,3,1,6]
    """
    # an outer loop to keep track of current elements
    for i in range(1, len(a)):
        cur = a[i]
        j = i
        while j > 0 and a[j - 1] > cur:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = cur


def selection_sort(a):
    """
    In-place O(n^2) sorting algorithm
    """
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[i]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]
    return a


def quick_sort(a):
    """
    A divide and conquer algorithm that involves partitioning up the input array based on a pivot into:
    l: sublist with elements less than the pivot,
    e: sublist with elements equal to the pivot,
    g: sublist with elements greater than the pivot

    Average case: O(n log n)
    Worst Case: O(n^2) if the smallest or largest element is chosen as the pivot.
    space: O(log n)
    """
    # base case
    n = len(a)
    if n < 2:
        return a

    # recursive case
    pivot = a[n - 1]
    left_partition = [el for el in a if el < pivot]
    equal_partition = [el for el in a if el == pivot]
    right_partition = [el for el in a if el > pivot]

    return quick_sort(left_partition) + equal_partition + quick_sort(right_partition)


def merge_sort(a):
    """
    All cases: O(n log n)
    Space: O(n)
    """
    # base case
    n = len(a)
    if n < 2:
        return a
    if n == 2:
        if a[0] > a[1]:
            return [a[1], a[0]]

    # recursive case
    mid = n // 2
    left = a[0:mid]
    right = a[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)
