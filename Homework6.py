#Python Home Work 6
# Пользователь вводит с клавиатуры три числа. В зависимости
# от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

num1 = int(input("Please input first number: "))
num2 = int(input("Please input second number: "))
num3 = int(input("Please input third number: "))
oper = int(input("If you want to sum press 1, if multiply press 2: "))
if oper != 1 and oper != 2:
    print("You type some wrong, try again.")
elif oper == 1:
    print(num1, "+", num2, "+", num3, "=", num1 + num2 + num3)
elif oper == 2:
    print(num1, "*", num2, "*", num3, "=", num1 * num2 + num3)
else:
    print("You type some wrong, try again.")
