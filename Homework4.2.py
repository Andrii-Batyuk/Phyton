#Python Home Work 4
#Пользователь вводит с клавиатуры три числа. В зависимости от выбора
#пользователя программа выводит на экран максимум из трёх,
#минимум из трёх или среднеарифметическое трёх чисел.

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

print("Maximum of this numbers is:")
if x > y and y > z:
    print(x)
elif x < y and y > z:
    print(y)
elif x < y and y < z:
    print(z)