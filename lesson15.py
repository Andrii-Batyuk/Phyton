






#
#
#
#
# #
# # l - [1,2,3,5,'FFF']
# # l = []
# # l - list()
#
# fruits = ['Apple', 'Pear', 'Peach', 'Mellon', 'Watermellon', 'Grape' ]
# # print(fruits[0])
# # print(fruits[-1])
# # print(fruits[0:4])
# # print(fruits[1, 3])
#
# # if fruits[0] == 'Apple':
# #     fruits[0] = 'Lemon'
# # print(fruits[0:6])
#
# print(fruits[::-1])
#
# fruits.append('Lemon')
# print(fruits)
#
# fruits.insert(5,'Onion')
# print(fruits)
#
# fruits.pop(4)
# print(fruits)
#
# fruits.remove('Peach')
# print(fruits)
#
# print(len(fruits))
#
# print('Onion' in fruits)
#
# new_fruits = fruits[:]
# new_fruits.pop(4)
# fruits.pop(1)
# print(new_fruits)
# print(fruits)



# Задание 1
# В списке целых, заполненном случайными числами
# вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и
# максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.

numbers = [3,5,23,-5,6,0,2,12,-5,9,-11,12,2,3,5,323,-5,6,2,-112,0,-5,9,-11,12,2]
sum_neg = 0
sum_even = 0
sum_odd = 0

for number in numbers:
    if number < 0:
        sum_neg = sum_neg + 1
    elif number % 2 == 0 and number != 0:
        sum_even = sum_even + 1
    elif number % 2 != 0 and number != 0:
        sum_odd  = sum_odd + 1

print(sum_even,sum_odd,sum_neg)

counter = 1

for i in numbers:
    if i % 3 == 0 and i != 0:
        counter = numbers[i] * counter
print(counter)


minimum = numbers[0]
maximum = numbers[0]
for index in numbers:
    if minimum > index:
        minimum = index
    elif maximum < index:
        maximum = index
print(minimum, maximum)


if minimum < maximum:
    print(numbers.index(12))
