#Python Home Work 4.1
#Пользователь вводит с клавиатуры три числа.
#В зависимости от выбора пользователя программа выводит
#на экран сумму трёх чисел или произведение трёх чисел.

x = int(input("Please input first number: "))
y = int(input("Please input second number: "))
z = int(input("Please input third number: "))
opr = str(input("If you want to sum, type + and if yo want to multiply, type * : "))
if opr == "+":
    print(x,"+", y, "+", z,"=", (x + y + z))
elif opr == "*":
    print(x,"*", y, "*", z,"=", (x * y * z))
else:
    print("You type something wrong...")