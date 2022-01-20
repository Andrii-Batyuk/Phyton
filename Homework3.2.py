#Python Home Work 3
#Пользователь вводит с клавиатуры номер месяца (1-12).
#Необходимо вывести на экран название месяца.
#Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

month = int(input("Enter number of month (1-12): "))
if month <= 0:
    print("You type value equal or below zero")
elif month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("You type value more than 12")