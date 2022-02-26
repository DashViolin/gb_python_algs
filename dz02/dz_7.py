import unittest


# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def arithmetic_seq_sum(n):
    result, seq_element = 0, 1
    for _ in range(n):
        result += seq_element
        seq_element += 1
    return result


def arithmetic_seq_sum_check(n):
    if n < 0:
        return 0
    return n * (n + 1) / 2


class TestProblem(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(arithmetic_seq_sum(100), arithmetic_seq_sum_check(100))

    def test_zero(self):
        self.assertEqual(arithmetic_seq_sum(0), arithmetic_seq_sum_check(0))

    def test_negative(self):
        self.assertEqual(arithmetic_seq_sum(-10), arithmetic_seq_sum_check(-10))
