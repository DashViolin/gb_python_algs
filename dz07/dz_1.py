# 1. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from unittest import TestCase
from random import randint
from random import choice


def quickselect_median(array):
    if array:
        return quickselect(array, len(array) // 2)
    return None


def quickselect(array, k):
    if len(array) == 1 and k == 0:
        return array[0]
    pivot = choice(array)
    lows = [el for el in array if el < pivot]
    highs = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


def pick_pivot(array):
    def chunked(items, chunk_size):
        return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

    if not array:
        return None
    if len(array) < 5:
        array = sorted(array)
        return array[len(array) // 2]
    chunks = chunked(array, 5)
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]
    sorted_groups = [sorted(chunk) for chunk in full_chunks]
    medians = [chunk[2] for chunk in sorted_groups]
    median_of_medians = quickselect_median(medians)
    return median_of_medians


class Tests(TestCase):
    def test_normal(self):
        m = randint(1, 10)
        length = 2 * m + 1
        rands = [randint(-9, 9) for _ in range(length)]
        print(rands)
        self.assertEqual(list(sorted(rands[:]))[m], quickselect_median(rands[:]))

    def test_empty(self):
        self.assertEqual(None, quickselect_median([]))