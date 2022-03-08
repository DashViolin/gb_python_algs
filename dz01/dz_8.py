# 8. Определить, является ли год, который ввел пользователем, високосным или не високосным.
def is_leap_year(year):
    # return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


print(is_leap_year(2021))
print(is_leap_year(2020))
