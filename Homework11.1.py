# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчи-
# тать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

# Variables
list = [5, 6, 7, 8, 9, 0, -1, 0, -123, 342, 0, 234, -23423, 0, 23, 23423, 564, 234, 324234, 6567, -452345, 0]
min = 0
max = 0
negative = 0
positive = 0
zero = 0
# Counting results in cycle
for i in list:
    if i > max:
        max = i
    if i < min:
        min = i
    if i == 0:
        zero += 1
    if i > 0:
        positive += 1
    if i < 0:
        negative += 1
# Printing results
print("Minimum:", min, "\nMaximum:", max, "\nNegative:", negative, "\nPositive:", positive, "\nZeroes:", zero)
