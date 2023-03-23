from math import log2


def issorted(lst):
    "determines whether a list is sorted"
    return not any(lst[i + 1] < lst[i] for i in range(len(lst) - 1))


def linear_scan(lst):
    """identify edge cases: list already sorted, at most 5 items out of place, list reverse sorted
    return a value for which edge case applies"""
    misplaced = 0
    for index in range(len(lst) - 1):
        if lst[index + 1] < lst[index]:
            misplaced += 1
    if misplaced == len(lst) - 1:
        return "Reverse"
    elif misplaced == 0:
        return "Sorted"
    elif misplaced <= 5:
        return "Insertion Sort"

    else:
        return "No edge case"


def reverse_list(lst):
    "reverses a list"
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst


def insertionsort(lst, start=0, end=None):
    "insertion sort algorithm"
    if end == None:
        end = len(lst)

    for i in range(end - 1):
        j = i + 1
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1


def quicksort(lst, start=0, end=None, depth=0):
    "quicksort algorithm"
    depth += 1
    if depth == int(2 * (log2(len(lst)) + 1)):
        mergesort(lst)
        tracker.add("mergesort")
        return lst

    if end == None:
        end = len(lst)

    if end - start <= 16:
        insertionsort(lst)
        tracker.add("insertionsort")
        if issorted(lst):
            return lst

    if end - start <= 1:
        return lst

    i = start
    j = end - 2
    pivot = end - 1
    while i < j:
        while lst[i] < lst[pivot]:
            i += 1
        while i < j and lst[j] >= lst[pivot]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    if lst[i] >= lst[pivot]:
        lst[i], lst[pivot] = lst[pivot], lst[i]
    # sort the left side of pivot
    quicksort(lst, start, pivot, depth)
    # sort the right side of the pivot
    quicksort(lst, end, pivot, depth)
    # if the list is already sorted by mergesort or insertion sort
    if not issorted(lst):
        quicksort(lst, pivot + 1, end, depth)


def mergesort(lst):
    "sorts list by dividing and sorting each divded list"
    if len(lst) <= 1:
        return lst

    median = len(lst) // 2
    left_side = lst[:median]
    right_side = lst[median:]

    mergesort(left_side)
    mergesort(right_side)

    i = 0
    j = 0
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            lst[i + j] = left_side[i]
            i += 1

        else:
            lst[i + j] = right_side[j]
            j += 1
    lst[i + j :] = left_side[i:] + right_side[j:]


# initializes a global variable to keep track of the algorithms used
tracker = set()


def magic_sort(lst):
    "efficiently sorts a list"

    result = linear_scan(lst)
    if result == "Reverse":
        reverse_list(lst)
        return {"reverse_list"}
    elif result == "Sorted":
        return {"List is already sorted"}
    elif result == "Insertion Sort":
        insertionsort(lst)
        return {"insertionsort"}
    else:
        tracker.add("quicksort")
        quicksort(lst)
        if tracker == {"quicksort", "insertionsort", "mergesort"}:
            tracker.clear()
            return {"quicksort", "insertionsort", "mergesort"}
        elif tracker == {"quicksort", "insertionsort"}:
            tracker.clear()
            return {"quicksort", "insertionsort"}
