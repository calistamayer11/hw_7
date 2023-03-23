from math import log2


def issorted(lst):
    return not any(lst[i + 1] < lst[i] for i in range(len(lst) - 1))


def linear_scan(lst):
    # identify edge cases: list already sorted, at most 5 items out of place, list reverse sorted
    # return a value for which edge case applies
    if lst == sorted(lst):
        return "Sorted"

    elif lst == sorted(lst, reverse=True):
        return "Reverse"
    else:
        misplaced = 0
        for index in range(len(lst) - 1):
            if lst[index] < lst[index + 1]:
                continue
            elif misplaced >= 5:
                # don't use insertion call something else
                break
            else:
                misplaced += 1
        if misplaced <= 5:
            return "Insertion Sort"


def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst


def insertionsort(lst):
    # new_list = []
    n = len(lst)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
    return lst

    # misplaced = 0
    # for index in range(len(lst)):
    #     if lst[index] < lst[index + 1]:
    #         continue
    #     elif misplaced >= 5:
    #         break
    #     else:
    #         misplaced += 1


# def quicksort(lst):
#     # start = 0
#     # pivot = len(lst) - 1
#     # end = pivot - 1
#     # while start < end:
#     #     while lst[start] < lst[pivot]:
#     #         start += 1
#     #     while start < end and lst[end] >= lst[pivot]:
#     #         end = -1
#     #     if start < end:
#     #         lst[start], lst[end] = lst[end], lst[start]

#     #     if lst[pivot] <= lst[start]:
#     #         lst[pivot], lst[start] = lst[start], lst[pivot]
#     #         pivot = start
# def partition(lst, start, end):
#     start = 0
#     pivot = len(lst) - 1
#     end = pivot - 1
#     while start < end:
#         while lst[start] < lst[pivot]:
#             start += 1
#         while start < end and lst[end] >= lst[pivot]:
#             end = -1
#         if start < end:
#             lst[start], lst[end] = lst[end], lst[start]


#         if lst[pivot] <= lst[start]:
#             lst[pivot], lst[start] = lst[start], lst[pivot]
#             pivot = start
# if lst[start] > pivot and lst[end] < lst[pivot]:
#     lst[start], lst[end] = lst[end], lst[start]
# start = start + 1
# end = end - 1
def partition(lst, start, end):
    pivot = lst[end]  # choose last element as pivot
    i = start - 1  # index of smaller element
    for j in range(start, end):
        # If current element is smaller than or equal to pivot
        if lst[j] <= pivot:
            # increment index of smaller element
            i += 1
            # swap arr[i] and arr[j]
            lst[i], lst[j] = lst[j], lst[i]
    # swap arr[i + 1] and arr[high] (pivot)
    lst[i + 1], lst[end] = lst[end], lst[i + 1]
    return i + 1


def quicksort(lst, start=0, end=None, depth=0):
    if end == None:
        end = len(lst)
    depth += 1
    if depth == int(2 * (log2(len(lst)) + 1)):
        mergesort(lst)
        tracker.add("mergesort")
        return lst

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
            # j -= 1
            i += 1
        while i < j and lst[j] >= lst[pivot]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    if lst[i] >= lst[pivot]:
        lst[i], lst[pivot] = lst[pivot], lst[i]
        # pivot = i

    # sort the left side of pivot
    quicksort(lst, start, pivot, depth)
    # sort the right side of the pivot
    quicksort(lst, end, pivot, depth)
    # if the list iis already sorted by mergesort or insertion sort
    if issorted(lst) == False:
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


if __name__ == "__main__":
    lst_2 = [i for i in range(100, 0, -5)]
    print(lst_2)
    quicksort(lst_2)
    print(lst_2)

# unordered = [7, -1, 5, 44, -3, 2, 10, 7, 0, 70, 7]
# print(unordered)
# # mergesort(unordered)
# quicksort(unordered)
# print(unordered)
