import unittest


# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def find_max_sum(numbers: list):
    digits_sum, num_with_max_sum = 0, 0
    for number in numbers:
        current_sum = 0
        number_copy = number
        number = abs(number)
        while number:
            digit = number % 10
            current_sum += digit
            number = number // 10
        if current_sum > digits_sum:
            digits_sum, num_with_max_sum = current_sum, number_copy
    return num_with_max_sum, digits_sum


class TestProblem(unittest.TestCase):
    def test_many(self):
        self.assertEqual(find_max_sum([123, 234, 124, -234]), (234, 9))

    def test_one(self):
        self.assertEqual(find_max_sum([-123]), (-123, 6))

    def test_zeros(self):
        self.assertEqual(find_max_sum([]), (0, 0))


if __name__ == '__main__':
    numbers = []
    while True:
        value = input('Введите число (для прекращения ввода оставьте поле пустым): ')
        if not value:
            break
        numbers.append(int(value))
    num_with_max_sum, digits_sum = find_max_sum(numbers)
    print(f'Число с максимальной суммой цифр: {num_with_max_sum}')
    print(f'Сумма цифр: {digits_sum}')
