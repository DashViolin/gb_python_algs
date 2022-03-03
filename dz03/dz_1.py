import unittest
from collections import defaultdict


# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def multiples():
    stats = defaultdict(int)
    for x in range(2, 100):
        for m in range(2, 10):
            if not x % m:
                stats[m] += 1
    return stats


class Solution(unittest.TestCase):
    def test(self):
        answer = {
            2: 49,
            3: 33,
            4: 24,
            5: 19,
            6: 16,
            7: 14,
            8: 12,
            9: 11,
        }
        self.assertEqual(multiples(), answer)
