"""Два списка целых заполняются случайными числами.
Необходимо:
■ Сформировать третий список, содержащий элементы
обоих списков; +
■ Сформировать третий список, содержащий элементы
обоих списков без повторений; +
■ Сформировать третий список, содержащий элементы
общие для двух списков; +
■ Сформировать третий список, содержащий только
уникальные элементы каждого из списков;
■ Сформировать третий список, содержащий только
минимальное и максимальное значение каждого из
списков."""

from random import randint
print("■  Два списка целых заполняются случайными числами.")
list_1 = [randint(-50, 50) for _ in range(15)]
list_2 = [randint(-50, 50) for _ in range(15)]

print(list_1)
print(list_2)


print("■ Сформировать третий список, содержащий элементы обоих списков;")

# list_3 = []
# for i in list_1:
#     list_3.append(i)
# for i in list_2:
#     list_3.append(i)

list_3 = list_1 + list_2
print(list_3)

print("■ Сформировать третий список, содержащий элементы обоих списков без повторений;")
nodublicate = []

for i in list_1:
    if i not in nodublicate:
        nodublicate.append(i)
for i in list_2:
    if i not in list_1 and i not in nodublicate:
        nodublicate.append(i)

print(nodublicate)


print("■ Сформировать третий список, содержащий элементы общие для двух списков;")
list_3 = []
for i in list_1:
    if i in list_1 and i in list_2:
        list_3.append(i)

print(list_3)

print("■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;.")
list_3 = []
for i in list_1:
    if i in list_3:
        list_3.remove(i)
        continue
    else:
        if i in list_2:
            continue
        else:
            list_3.append(i)
for i in list_2:
    if i in list_3:
        list_3.remove(i)
    else:
        if i in list_1:
            continue
        else:
            list_3.append(i)


print(list_3)


print("■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.")

min1 = 0
max1 = 0
min2 = 0
max2 = 0
min_max_list = []

for i in list_1:
    if i < min1:
        min1 = i
min_max_list.append(min1)

for a in list_1:
    if a > max1:
        max1 = a
min_max_list.append(max1)

for q in list_2:
    if q < min2:
        min2 = q
min_max_list.append(min2)

for q in list_2:
    if q > max2:
        max2 = q
min_max_list.append(max2)

print(min_max_list)


list_5 = [for i in range(18)]