"""Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world...
if you do so, you are insulting yourself.”
Bill Gates
"""
print("Task 1")

def function1():
    print("“Don't compare yourself with anyone in this world...\n if you do so, you are insulting yourself.”\n\t\t\t\t\t\t\t\t\t\tBill Gates")
function1()

"""Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все четные числа
между ними."""

print("Task 2")

def function2(a, b):
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i)
function2(4, 8)


"""Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны ква-
драта, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
"""

print("Task 3")

def function3(a, b, c):


function2(4, 8, True)

"""Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров."""


print("Task 4")

def function4(a, b, c, d, e):


function2(4, 8, 0, -2, 1)

"""Задание 5
Напишите функцию, которая возвращает произве-
дение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапа-
зона перепутаны (например, 5 — верхняя граница, 25 —
нижняя граница), их нужно поменять местами."""

print("Task 5")
def function5(a, b):
    if a < b:
        for i in range(a+1, b+1):
            a = a * i
        print(a)
    elif a > b:
        for i in range(b+1, a+1):
            b = b * i
        print(b)

function5(5, 3)
function5(3, 5)

"""Задание 6
Напишите функцию, которая считает количество
цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4."""

print("Task 6")
def function6(a):
    counter = 0
    for i in str(a):
        counter = counter + 1
    print(counter)
function6(123410)



"""Задание 7
Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве пара-
метра. Если число палиндром нужно вернуть из функции
true, иначе false.
«Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например,
123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром"""

print("Task 7")

def function7(a):
    # Variables
    string = str(a)
    counter = 0
    delim = 1
    # Counting length of the string:
    for i in range(len(string)):
        counter += 1
    # Enumerate is string is even and calculate middle of the string
    if counter % 2 == 0:
        delim = counter // 2
    # Compare slices of the string and print results
        if (string[:delim]) == (string[:delim-1:-1]):
            print((string[:delim]), "is equal", (string[delim:]))
        elif (string[:delim]) != (string[:delim-1:-1]):
            print((string[:delim]), "is NOT equal", (string[delim:]))
    else:
        print("This string is odd!")

function7(884466333222222222222222222222222222222222222222222222222222222333664488)
function7("asdfewrdwerdsf")
function7("123 asd                                              dsa 321")
function7("123")


