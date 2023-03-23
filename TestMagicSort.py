import unittest
import random
from MagicSort import (
    linear_scan,
    reverse_list,
    insertionsort,
    quicksort,
    mergesort,
    magic_sort,
)


class Test_linear_scan(unittest.TestCase):
    def test_linear_scan(self):
        sorted_list = [1, 2, 3, 4, 5]
        self.lst = [i for i in range(101)]
        self.lst_reversed = [i for i in range(100, 0, -1)]
        self.lst_random = [random.randint(0, 100) for i in range(101)]
        self.lst_2 = [7, -1, 5, 44, -3, 2, -1, 0]
        # self.lst2[:10] =

        self.assertEqual(linear_scan(self.lst), "Sorted")
        # self.assertEqual(linear_scan(sorted_list), sorted_list)
        self.assertEqual(linear_scan(self.lst_reversed), "Reverse")
        self.assertEqual(linear_scan(self.lst_2), "Insertion Sort")


class Test_reverse_list(unittest.TestCase):
    def test_reverse(self):
        random_list = [2, 4, 8, 1, 2]
        reverse_random_list = [2, 1, 8, 4, 2]
        self.assertEqual(reverse_list(random_list), reverse_random_list)


class Test_insertionsort(unittest.TestCase):
    def test_insertion_sort(self):
        "test for insertion sort"
        self.lst = [15, 1, 14, 2, 13, 3, 12, 5]
        self.lst_2 = [i for i in range(25, 0, -2)]

        insertionsort(self.lst)
        self.assertEqual(self.lst, [1, 2, 3, 5, 12, 13, 14, 15])

        insertionsort(self.lst_2)
        self.assertEqual(self.lst_2, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])


class Test_quicksort(unittest.TestCase):
    "test for quicksort"

    def test_quicksort(self):
        self.lst = [3, 43, 2, 14, 65, 42, 13]
        quicksort(self.lst)
        self.assertEqual(self.lst, [2, 3, 13, 14, 42, 43, 65])


class Test_mergesort(unittest.TestCase):
    "test for mergesort"

    def test_mergesort(self):
        self.lst = [3, 43, 2, 14, 65, 42, 13]
        self.lst_2 = [i for i in range(100, 0, -5)]

        mergesort(self.lst)
        self.assertEqual(self.lst, [2, 3, 13, 14, 42, 43, 65])

        mergesort(self.lst_2)
        self.assertEqual(
            self.lst_2,
            [
                5,
                10,
                15,
                20,
                25,
                30,
                35,
                40,
                45,
                50,
                55,
                60,
                65,
                70,
                75,
                80,
                85,
                90,
                95,
                100,
            ],
        )


class Test_magicsort(unittest.TestCase):
    "tests magicsort with all cases"

    def test_magicsort(self):

        n = int(1e5)

        self.lst = [(n - i) for i in range(n)]
        self.assertEqual(magic_sort(self.lst), {"reverse_list"})

        self.lst_2 = [(n - i) for i in range(n)]
        self.lst_2[:6] = [-1, -2, -3, -4, -5, -6]
        self.assertEqual(
            magic_sort(self.lst_2), {"quicksort", "insertionsort", "mergesort"}
        )
        self.lst_3 = [i for i in range(100)]
        self.assertEqual(magic_sort(self.lst_3), {"List is already sorted"})

        self.lst_4 = [90, 1, 2, 70, 3, 4, 5, 2, 567, 45, 23, 1, 2, 13, 1, 2, 3, 4, 4]

        self.assertEqual(magic_sort(self.lst_4), {"quicksort", "insertionsort"})

        self.lst_5 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(magic_sort(self.lst_5), {"insertionsort"})


unittest.main()
