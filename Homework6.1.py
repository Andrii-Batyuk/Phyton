# Пользователь вводит с клавиатуры три числа. В зависимости
# от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или
# среднеарифметическое трёх чисел.

num1 = int(input("Please input first number: "))
num2 = int(input("Please input second number: "))
num3 = int(input("Please input third number: "))
oper = int(input("If you want to see maximum press 1, if minimum press 2, if average press 3: "))
if oper != 1 and oper != 2 and oper != 3:
    print("You type some wrong, try again.")
elif (oper == 1 and num1 == num2 == num3) or (oper == 2 and num1 == num2 == num3):
    print("This numbers are equal, so answer is:", num1)
elif (oper == 1 and num1 >= num2) and (oper == 1 and num1 >= num3):
    print("Maximum of these numbers is:", num1)
elif (oper == 1 and num2 >= num1) and (oper == 1 and num2 >= num3):
    print("Maximum of these numbers is:", num2)
elif (oper == 1 and num3 >= num1) and (oper == 1 and num3 >= num2):
    print("Maximum of these numbers is:", num3)
elif (oper == 2 and num1 <= num2) and (oper == 2 and num1 <= num3):
    print("Minimum of these numbers is:", num1)
elif (oper == 2 and num2 <= num1) and (oper == 2 and num2 <= num3):
    print("Minimum of these numbers is:", num2)
elif (oper == 2 and num3 <= num1) and (oper == 2 and num3 <= num2):
    print("Minimum of these numbers is:", num3)
elif oper == 3:
    print("Average of these numbers is:", (num1 + num2 + num3)/3)
else:
    print("You type some wrong, try again.")

