# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,Домашнее задание
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»


while True:
    num = int(input("Input some number: "))
    if num > 0 and num != 7:
        print("Number is positive")
    elif num < 0 and num != 7:
        print("Number is negative")
    elif num == 0 and num != 7:
        print("Number is equal to zero")
    elif num == 7:
        break
print("Good bye!")