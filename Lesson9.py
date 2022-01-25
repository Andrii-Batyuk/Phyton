# for i in ():
#     print(i, end=" ")
#
#
# for i in 'Andrii Batiuk':
#     print(i, end=' ')
# print()
#
# for i in range(10):
#     print(i, end=' ' )

# Задание 2
# Пользователь вводит с клавиатуры два числа. Нужно
# показать все нечетные числа в указанном диапазоне.

# a = int(input("Input beginning of the range: "))
# b = int(input("Input end of the range: "))
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i, end=' ')



# Задание 4
# Пользователь вводит с клавиатуры два числа. Нужно показать все числа в указанном диапазоне в порядке
# убывания.

# a = int(input("Input end of the range: "))
# b = int(input("Input start of the range: "))
# for i in range(b, a  -1, -1 ):
#     print(i, end=' ')



# # Задание 5
# # Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне.
# # Если границы диапазона указаны неправильно требуется
# # произвести нормализацию границ. Например, пользователь ввел 33 и 13, требуется нормализация после которой
# # начало диапазона станет равно 13, а конец 33.
#
# a = int(input("Input start of the range: "))
# b = int(input("Input end of the range: "))
#
# if b < a:
#     for i in range(b, a +1 ):
#         if i % 2 != 0:
#             print(i, end=' ')
# elif a < b:
#     for i in range(a, b +1 ):
#         if i % 2 != 0:
#             print(i, end=' ')
# else:
#     print("You type equal numbers.")

# Задание 2
# Пользователь вводит с клавиатуры число. Требуется
# посчитать факториал числа. Например, если введено 3,
# факториал числа 1*2*3 = 6.
# Формула для расчета факториала: n! = 1*2*3…*n, где
# n — число для расчета факториала.
# Задание 3
# Пользователь вводит с клавиатуры длину линии.
# Нужно отобразить на экране горизонтальную линию
# из *, указанной длины.
# Например, если было введено 7, тогда вывод на экран
# будет такой: *******.
# Задание 4
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране горизонтальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и &, тогда вывод на
# экран будет такой: &&&&&.
# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать сумму чисел в указанном диапазоне, а также
# среднеарифметическое.

#
# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать сумму чисел в указанном диапазоне, а также
# среднеарифметическое.

# a = int(input("Input start of the range: "))
# b = int(input("Input end of the range: "))
# count = -1
# sum = 0
#
# for i in range(a - 1, b + 1, 1):
#     sum = sum + i
#     count = count + 1
# print("Sum:", sum)
# print("Count:", count)
# print("Average:", sum / count)


# a = 1
# b = 10
# for i in range(a,b+1):
#
#     if i == 5:
#         continue
#     print(i, end=' ')

# a = 5
# symbol = "*"
# for i in range(a):
#     print(symbol *  a)



# a = 5
# b = 5
# symbol = "!"
# space = " "
#
# for i in range(b):
#     print(symbol, )
# for i in range(a):
#     print(symbol, ((b - 2) * space), symbol)
# # for i in range(b):
# #     print(symbol, end="")

# import random
# width = 3
# height = 3
# sym = random.randint(1, 9)
# for i in range(height):
#     print(f"|-{sym}-" * width, end='|\n')

# import random
# width = 3
# height = 3
# sym = random.randint(1, 9)
# for i in range(height):
#     print(f"|-{sym}-" * width, end='|\n')














import random

width = 3
height = 3
symbol = random.randint(1, 9)

for i in range(height):
    print(f"|-{symbol}-" * width, end="|\n")


# import os
#
# osname = os.name
# env = os.environ
# login = os.getlogin()
# print(osname)
# print(env)
# print(login)
