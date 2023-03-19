from math import log2


lst = []


def linear_scan(lst):
    # identify edge cases: list already sorted, at most 5 items out of place, list reverse sorted
    # return a value for which edge case applies
    if lst == lst.sort():
        return lst
    elif lst == lst.sort(reverse=True):
        return reverse_list(lst)
    else:
        misplaced = 0
        for index in range(len(lst)):
            if lst[index] < lst[index + 1]:
                continue
            elif misplaced >= 5:
                # don't use insertion call something else
                break
            else:
                misplaced += 1
        if misplaced <= 5:
            return insertionsort(lst)


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


def quicksort(lst, start, end):
    if start < end:
        # partition the array
        p = partition(lst, start, end)
        # recursively sort elements before partition and after partition
        quicksort(lst, start, p - 1)
        quicksort(lst, p + 1, end)


# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array:", arr)


def mergesort(lst):
    pass


def magic_sort(lst):
    pass
