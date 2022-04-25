# Пользователь вводит с клавиатуры два числа (начало
# и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно вывести
# слово Buzz. Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
# само число.


a = int(input("Input start of the range: "))
b = int(input("Input end of the range: "))

if a < b:

    for i in range(a, b+1):
        if i % 3 == 0:
            print("Fizz,", end='  ')
        if i % 5 == 0:
            print("Buzz,", end='  ')
        if i % 5 == 0 and i % 3 == 0:
            print("Fizz Buzz,", end='  ')
        if i % 3 != 0 and i % 5 != 0:
            print(i, end=',  ')
else:
    print("You input wrong range. Try again.")