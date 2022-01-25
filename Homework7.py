# Пользователь вводит с клавиатуры два числа (нача-
# ло и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.

num1 = int(input("Input beginning of the range: "))
num2 = int(input("Input end of the range: "))

if num1 > num2:
    print("You typed wrong values, try again. ")
while num2 >= num1:

    if num2 % 7 == 0:
        print(num2, end=" ",)

    num2 = num2 - 1
