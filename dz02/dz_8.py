import unittest


# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def count_numbers(numbers: list, digit: int):
    result = 0
    for number in numbers:
        while number:
            current_digit = number % 10
            if current_digit == digit:
                result += 1
            number = number // 10
    return result


class TestProblem(unittest.TestCase):
    def test_one(self):
        self.assertEqual(count_numbers([123, 234, 124, 234], 2), 4)

    def test_two(self):
        self.assertEqual(count_numbers([1], 1), 1)

    def test_three(self):
        self.assertEqual(count_numbers([1], 2), 0)


if __name__ == '__main__':
    n = int(input('Введите количество чисел: '))
    numbers = []
    for _ in range(n):
        numbers.append(int(input('Введите число: ')))
    digit = int(input('Введите цифру для подсчета: '))
    print(f'Количество цифр {digit} в введенной последовательности: {count_numbers(numbers, digit)}')
