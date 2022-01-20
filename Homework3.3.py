#Python Home Work 3.3
#Пользователь вводит с клавиатуры число. Если число
#больше нуля нужно вывести надпись «Number is positive»,
#если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»

number = int(input("Please input some number: "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is equal to zero")
