# Пользователь вводит с клавиатуры числа. Програм-
# ма должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»
summ = 0
maximum = 0
minimum = 100000000000000000000000000000000000000
while True:
    num = int(input("Input some number: "))
    summ = summ + num
    print("Sum is: ", summ)
    if num > maximum:
        maximum = num
    print("Maximum is: ", maximum)
    if num < minimum:
        minimum = num
    print("Minimum is: ", minimum)
    if num == 7:
        break
print("Good Bye!")

