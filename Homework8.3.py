# Пользователь вводит любое целое число. Необхо-
# димо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.


# x = int(input("Input some number: "))
# string = str(x)
#
# for i in range(len(string)):
#
#     if string[i] == "3" or string[i] == "6":
#         continue
#     print(string[i], end="")
#
#
# # string = string.replace("3", "")
# # string = string.replace("6", "")
# # print(string)


# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch ,end='')
#     # Line of code.

# for digit in "0165031806510":
#     if digit == "0":
#         digit = 'X'
#     print(digit, end='')
#
# print()
#
# for digit in "0165031806510":
#     if digit == "0":
#         print("X", end="")
#         continue
#     print(digit, end="")

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)