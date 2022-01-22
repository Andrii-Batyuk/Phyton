# i = 1
# while i < 10:
#     print("Andrey")
#     i+= 1

# print("Andrey\n" * 10)

# i = 0
# word = ''
# while i < 20:
#     #word = ''
#     i = i + 1
#     word = word + str(i)
#     print(word)

# a = 10
# b = 0
# while a >= b:
#     print(a)
#     a = a - 1

# a = int(input("Input value"))
# b = int(input("Input value"))
# while a <= b:
#     if a % 2 == 0:
#         print(a)
#     a = a + 1

# a = int(input("Input value"))
# b = int(input("Input value"))
#
# if a < b:
#  while a <= b:
#      if a % 2 != 0:
#          print(a)
#      a = a + 1
# elif b < a:
#     while b <= a:
#         if b % 2 != 0:
#             print(b)
#         b = b + 1

# a = int(input("Input first value"))
# b = int(input("Input first value"))
# sum = 0
# while a <= b:
#     sum = sum + a
#     a = a + 1
#     print(sum)

# a = int(input("Input first value"))
# b = 0
#
# while a > b:
#     print(a//(a-1))
#     a = a - 1

# Задание 3
# Пользователь вводит с клавиатуры длину линии.
# Нужно отобразить на экране горизонтальную линию
# из *, указанной длины.
# Например, если было введено 7, тогда вывод на экран
# будет такой: *******.
# a = int(input("Input first value"))
# while a > 0:
#     print("*",end='')
#     a = a - 1

# Задание 4
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране горизонтальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и &, тогда вывод на
# экран будет такой: &&&&&.

# a = int(input("Input lenght of the line value: "))
# b = str(input("Input symbol of the line: "))
# while a > 0:
#     print(b,end='')
#     a = a - 1
# print()
# print("Andrey")

#Guess my number

# import random
# tryes = 5
# secret_number = random.randint(1,20)
# guess_num = 0
#
# while secret_number != guess_num and tryes >= 1:
#     guess_num = int(input("Input guess number"))
#     if guess_num == secret_number:
#         print("You win!")
#     tryes = tryes - 1
# if secret_number != guess_num and tryes == 0:
#     print("You loose")

# Показать таблицу умножения для числа, введенного
# пользователем. Например, если пользователь вводит
# число 7, нужно показать:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21

num = int(input("Input value (1-10): "))
a = 1
if num == 0:
    print("You type zero")
while a <= 10:
    print(f"{num} * {a} =", num * a)
    a = a + 1