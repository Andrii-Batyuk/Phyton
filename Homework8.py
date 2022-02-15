# Задание 1
# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.

x = int(input("Input first number: "))
y = int(input("Input first number: "))
mult = x

# First solution
print(x ** y)
# Second solution
for i in range(y-1):
    x = x * mult
    print(x)