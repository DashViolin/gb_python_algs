import unittest


# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def nums(number: int) -> (int, int):
    """
    Считает четные и нечетные цифры введенного натурального числа.
    :param number: натуральное число
    :return: odds, evens - количествно нечетных и четных цифр соответственно.
    """
    if number < 0:
        raise ValueError('Только натуральные числа.')
    odds = 0
    evens = 0
    if number == 0:
        evens += 1
    while number:
        digit = number % 10
        if digit % 2:
            odds += 1
        else:
            evens += 1
        number = number // 10
    return odds, evens


class TestProblem(unittest.TestCase):
    def test_normal(self):
        self.assertEqual((3, 2), nums(12345))

    def test_zero(self):
        self.assertEqual((0, 1), nums(0))

    def test_negative(self):
        self.assertRaises(ValueError, nums, -1)
