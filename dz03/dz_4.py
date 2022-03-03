import unittest
from random import randrange


# 4. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def find_two_minimal_pythonic(l: list) -> tuple:
    if l and len(l) > 1:
        return tuple(list(sorted(l))[:2])
    return None, None


def find_two_minimal(l: list) -> tuple:
    if l and len(l) > 1:
        min_1, min_2 = float('inf'), float('inf')
        min_1_index = 0
        for i, x in enumerate(l):
            if x < min_1:
                min_1 = x
                min_1_index = i
        for i, x in enumerate(l):
            if x < min_2 and i != min_1_index:
                min_2 = x
        return min_1, min_2
    return None, None


class Solution(unittest.TestCase):
    def test_normal(self):
        rands = [randrange(-9, 10) for _ in range(10)]
        self.assertEqual(find_two_minimal(rands), find_two_minimal_pythonic(rands))

    def test_non_negatives(self):
        rands = [randrange(10) for _ in range(10)]
        self.assertEqual(find_two_minimal(rands), find_two_minimal_pythonic(rands))

    def test_empty(self):
        rands = []
        self.assertEqual(find_two_minimal(rands), find_two_minimal_pythonic(rands))
