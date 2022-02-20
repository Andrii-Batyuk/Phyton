# Задание 1
# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палин-
# дром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.

# Variables
a = str(input("Input some string: "))
b = ''
c = ''
# Cycle for removing spaces
for i in a:
    if i == ' ':
        continue  # Removing spaces
    b = b + i
c = b[::-1]  # Create reverse string
# Compare with lowercase and print results
if c.lower() == b.lower():
    print(a, "is palindrome!")
else:
    print(a, "is not palindrome((")


