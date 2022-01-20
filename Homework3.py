#Python Home Work 3
day = int(input("Enter number of the day to see it's name ( 1 -7 ): "))
if day <= 0:
    print("You input value equal zero or below!")
elif day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("You input value more than 7")