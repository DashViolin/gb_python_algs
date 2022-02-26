# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
char_one = input("Enter char 1: ")
char_two = input("Enter char 2: ")
shift = ord('a') - 1
print(f'Position of char one: {ord(char_one.lower()) - shift}')
print(f'Position of char two: {ord(char_two.lower()) - shift}')
print(f'Chars in interval: {abs(ord(char_one.lower()) - ord(char_two.lower()))}')
