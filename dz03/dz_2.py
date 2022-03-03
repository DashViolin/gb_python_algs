import unittest
from random import randrange


# 2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def min_max_swap_pythonic(l: list) -> None:
    min_index, max_index = l.index(min(l)), l.index(max(l))
    l[min_index], l[max_index] = l[max_index], l[min_index]


def min_max_swap(l: list) -> None:
    min_index, max_index = l[-1], l[-1]
    for i, x in enumerate(l):
        if x > l[max_index]:
            max_index = i
        elif x < l[min_index]:
            min_index = i
    l[min_index], l[max_index] = l[max_index], l[min_index]


class Solution(unittest.TestCase):
    def test(self):
        rands_1 = [randrange(10) for _ in range(10)]
        rands_2 = rands_1[:]
        self.assertEqual(min_max_swap(rands_1), min_max_swap_pythonic(rands_2))
