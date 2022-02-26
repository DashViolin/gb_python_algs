import unittest


# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

def seq_sum(n):
    result, seq_element = 0, 1
    for _ in range(n):
        result += seq_element
        seq_element /= -2
    return result


class TestProblem(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(0.666666666045785, seq_sum(30))

    def test_zero(self):
        self.assertEqual(0, seq_sum(0))

    def test_negative(self):
        self.assertEqual(0, seq_sum(-30))
