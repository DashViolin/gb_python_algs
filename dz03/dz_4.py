import unittest
from random import randrange


# 4. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def find_two_minimal_pythonic(l: list) -> tuple:
    if l and len(l) > 1:
        return tuple(sorted(l)[:2])
    return None, None


def find_two_minimal(l: list) -> tuple:
    # if l and len(l) > 1:
    #     min_1, min_2 = float('inf'), float('inf')
    #     min_1_index = 0
    #     for i, x in enumerate(l):
    #         if x < min_1:
    #             min_1, min_1_index = x, i
    #     for i, x in enumerate(l):
    #         if x < min_2 and i != min_1_index:
    #             min_2 = x
    #     return min_1, min_2
    # return None, None

    # Комментарий:
    # "Посмотри здесь решение некоторых номеров https://pastebin.com/4q6Se7Yp.
    # 4 номер точно проще можно, как в ссылке выше"
    # Ответ: по ссылке выше алгоритм некорректный (проблема с начальными значениями), доработанный приведен ниже:
    if l and len(l) > 1:
        first_min, second_min = (l[0], l[1]) if l[0] < l[1] else (l[1], l[0])
        for i in range(2, len(l)):
            if l[i] < first_min:
                second_min = first_min
                first_min = l[i]
            elif l[i] < second_min:
                second_min = l[i]
        return first_min, second_min
    return None, None


class Solution(unittest.TestCase):
    def test_normal(self):
        rands = [randrange(-9, 10) for _ in range(10)]
        self.assertEqual(find_two_minimal_pythonic(rands), find_two_minimal(rands))

    def test_non_negatives(self):
        rands = [randrange(10) for _ in range(10)]
        self.assertEqual(find_two_minimal_pythonic(rands), find_two_minimal(rands))

    def test_empty(self):
        rands = []
        self.assertEqual(find_two_minimal_pythonic(rands), find_two_minimal(rands))
