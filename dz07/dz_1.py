# 1. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from unittest import TestCase
from random import randint


# MergeSort (from https://www.programiz.com/dsa/merge-sort)
def merge_sort(array):
    if len(array) <= 1:
        return None
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def get_median(items: list):
    if items:
        merge_sort(items)
        return items[len(items) // 2]
    return None


class Tests(TestCase):
    def test_normal(self):
        m = randint(1, 10)
        length = 2 * m + 1
        rands = [randint(-9, 9) for _ in range(length)]
        print(rands)
        self.assertEqual(list(sorted(rands[:]))[m], get_median(rands[:]))

    def test_empty(self):
        self.assertEqual(None, get_median([]))
