from random import randint

"""Курс: «Введение в язык
программирования Python
Модуль 5. Функции.
Тема: Функции. Часть 2
"""

"""Задание 1
Напишите функцию, вычисляющую произведение
элементов списка целых. Список передаётся в качестве па-
раметра. Полученный результат возвращается из функции."""

print("Task 1")


def multiply_list(a):
    print(f'List fo multiply {a}')
    mult = 1
    for i in range(len(a)):
        mult *= a[i]
        print(mult)
    print(f'Multiply of list is {mult}')


multiply_list([randint(1, 100) for i in range(10)])


"""Задание 2
Напишите функцию для нахождения минимума в
списке целых. Список передаётся в качестве параметра.
Полученный результат возвращается из функции."""

print()
print("Task 2")
def minimal_list(b):
    print(f'List for finding minimal element {b}')
    minimum = 0
    for i in range(len(b)):
        if minimum > b[i]:
            minimum = b[i]
    print(f'Minimum number of the list is {minimum}')


minimal_list([randint(-100, 100) for a in range(10)])


"""Задание 3
Напишите функцию, определяющую количество про-
стых чисел в списке целых. Список передаётся в качестве
параметра. Полученный результат возвращается из функции."""


print()
print("Task 3")
primes = []
numbers_list = [simpl for simpl in range(1, 50)]
print(numbers_list)


def prime_fun(arg):

    for possiblePrime in range(2, len(arg)):
        isprime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isprime = False
        if isprime:
            primes.append(possiblePrime)
    print(f'Prime numbers are: {primes}')


prime_fun(numbers_list)


"""Задание 4
Напишите функцию, удаляющую из списка целых
некоторое заданное число. Из функции нужно вернуть
количество удаленных элементов."""


print()
print("Task 4")

deleting_list = [randint(1, 10) for ii in range(30)]
print(f'List for deleting some number {deleting_list}')
some_number = randint(1, 10)
print(f'Some number for deleting is {some_number}')


def deleting_fun(arg1, arg2):
    # Bad solution
    # counter = 0
    # for aa in arg1:
    #     if aa == arg2:
    #         arg1.remove(arg2)
    #         counter += 1
    counter = 0
    for index in range(len(arg1)):
        if arg1[index-counter] == arg2:
            del arg1[index-counter]
            counter += 1

    print(f'In list {arg1} element {some_number} was deleted {counter} times')


deleting_fun(deleting_list, some_number)


"""Задание 5
Напишите функцию, которая получает два списка в
качестве параметра и возвращает список, содержащий
элементы обоих списков."""

print()
print("Task5")
lst_a = [randint(0, 100) for x in range(10)]
lst_b = [randint(0, 100) for y in range(10)]
print(f'List 1 {lst_a}')
print(f'List 2 {lst_b}')


def union_list(lst_1, lst_2 ):
    lst_3 = lst_1 + lst_2
    print(f'Union list is {lst_3}')


union_list(lst_a, lst_b)


"""Задание 6
Напишите функцию, высчитывающую степень каждого
элемента списка целых. Значение для степени передаётся
в качестве параметра, список тоже передаётся в качестве
параметра. Функция возвращает новый список, содержа-
щий полученные результаты."""

print()
print("Task 6")

arg_lst = [randint(0, 100) for p in range(10)]
power = randint(1, 10)
print(f'List with numbers {arg_lst}')
print(f'Power {power}')


def power_list(arg, pwr):
    new_lst = [unit ** pwr for unit in arg]
    print(new_lst)


power_list(arg_lst, power)
