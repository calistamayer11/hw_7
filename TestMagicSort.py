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
        self.lst_random = [random.randint(0, 100) for i in range(101))]
        self.lst_2 = self.lst[:]
        self.lst2[:10] = 
        self.assertEqual(linear_scan(sorted_list), sorted_list)


class Test_reverse_list(unittest.TestCase):
    def test_reverse(self):
        random_list = [2, 4, 8, 1, 2]
        reverse_random_list = [2, 1, 8, 4, 2]
        self.assertEqual(reverse_list(random_list), reverse_random_list)


class Test_insertionsort(unittest.TestCase):
    pass


# def test_insertion(self):


class Test_quicksort(unittest.TestCase):
    pass


class Test_mergesort(unittest.TestCase):
    pass


class Test_magicsort(unittest.TestCase):
    pass


unittest.main()
