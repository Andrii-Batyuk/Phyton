# Пользователь вводит любое целое число. Необхо-
# димо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.


x = int(input("Input some number: "))
string = str(x)

for i in range(len(string)):

    if string[i] == "3" or string[i] == "6":
        continue
    print(string[i], end="")


# string = string.replace("3", "")
# string = string.replace("6", "")
# print(string)


