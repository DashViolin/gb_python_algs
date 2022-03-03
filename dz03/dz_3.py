import unittest
from random import randrange


# 3. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
def find_min_neg(l: list) -> tuple:
    max_neg_value, max_neg_index = float('-inf'), None
    for i, x in enumerate(l):
        if x < 0:
            if x > max_neg_value:
                max_neg_index, max_neg_value = i, x
    if max_neg_index:
        return max_neg_value, max_neg_index
    return None, None


def find_min_neg_pythonic(l: list) -> tuple:
    negatives = list(filter(lambda x: x < 0, l))
    max_neg_value = max(negatives) if negatives else None
    max_neg_index = l.index(max_neg_value) if max_neg_value else None
    return max_neg_value, max_neg_index


class Solution(unittest.TestCase):
    def test_normal(self):
        rands = [randrange(-9, 10) for _ in range(10)]
        self.assertEqual(find_min_neg(rands), find_min_neg_pythonic(rands))

    def test_non_negatives(self):
        rands = [randrange(10) for _ in range(10)]
        self.assertEqual(find_min_neg(rands), find_min_neg_pythonic(rands))
