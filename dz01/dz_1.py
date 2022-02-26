# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
user_input = input("Enter digit: ")
number = int(user_input)

sum_result = 0
prod_result = 1
while number:
    digit = number % 10
    sum_result += digit
    prod_result *= digit
    number = number // 10

print(sum_result)
print(prod_result)
