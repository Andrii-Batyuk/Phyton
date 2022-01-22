#Python Home Work 3.4
#Пользователь вводит два числа. Определить, равны
#ли эти числа, и, если нет, вывести их на экран в порядке
#возрастания.

a = int(input("Input first number: "))
b = int(input("Input second number: "))

if a == b:
    print("This numbers are equal:", a, "=", b)
elif a > b:
    print(a,b)
elif a < b:
    print(b,a)