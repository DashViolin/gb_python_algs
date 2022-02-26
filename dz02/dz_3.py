# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)
import unittest


def reverse(number: int) -> int:
    result = 0
    while number > 0:
        reminder = number % 10
        result = result * 10 + reminder
        number = number // 10
    return result


class TestProblem(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(9854, reverse(4589))

    def test_one(self):
        self.assertEqual(5, reverse(5))

    def test_negative(self):
        self.assertEqual(0, reverse(-4321))


