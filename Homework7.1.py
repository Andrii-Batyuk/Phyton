# Пользователь вводит с клавиатуры два числа (нача-
# ло и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

a = int(input("Input start of the range: "))
b = int(input("Input end of the range: "))
counter = b

if a < b:

    for i in range(a, b+1):
        print(i, end=' ')
    print()

    while counter >= a:
        print(counter, end=' ')
        counter = counter - 1
    print()

    for i in range(a, b+1):
        if i % 7 == 0:
            print(i, end=' ')
    print()

    for i in range(a, b+1):
        if i % 5 == 0:
            print(i, end=' ')
    print()

else:
    print("You input wrong range. Try again. ")