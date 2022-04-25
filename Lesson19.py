# Functions

# def myfunction(myvar):
#     print(myvar + 'Hello')
# myfunction('kldsf')

# def simple(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# l = [1, 2, 3]
# print(l.pop())
# print(l.append(4))
#
# def pop(somelist):
#     return somelist.pop()
#
# def append(somelist,data):
#     somelist.append(data)
#
#
# l = [1,2,3,4,5,6,7,8,9]
# print(pop(l))
# print(append(l,0))
# print(l)

# def calc(a, b):
#     return a + b
#
# print(calc(234, 23423))
#
# import math
# import turtle
# def xt(t):
#     return 16 * math.sin(t) **3
# def yt(t):
#     return 13 * math.cos(t) - 5 * \
#             math.cos(2 * t) - 2 * \
#             math.cos(3 * t) - \
#             math.cos(4 * t)
# t = turtle.Turtle()
# t.speed(500)
# turtle.colormode(255)
# turtle.Screen().bgcolor(0, 0, 0)
# for i in range(2550):
#     t.goto((xt(i) * 20, yt(i) * 20))
#     t.pencolor((255-i) % 255, i % 255, (255+i)//2%255)
#     t.goto(0, 0)
# t.hideturtle()
# turtle.update()
# turtle.mainloop()

# def custom_range(start,finish=False,step=False):
#     numbers = []
#     if finish:
#         while start < finish:
#             numbers.append(start)
#             if step:
#                 start = start + step
#             else:
#                 start = start + 1
#     else:
#         while 0 < start:
#             numbers.appens(start)
#             start = start + 1
#
# custom_range(1,20)

# [19:17] Буйлук Андрей
# Задание 7
# Напишите функцию, которая проверяет является
# ли шестизначное число «счастливым». Число передаётся в качестве параметра. Если число счастливое нужно
# вернуть из функции true, иначе false.
# «Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна сумме трёх вторых
# цифр. Например, 123420 – счастливое 1+2+3 = 4+2+0,
# а 723422 – несчастливое 7+2+3 != 4+2+2.

#
# def lucky_number(number):
#     number = str(number)
#     if len(number) == 6 and number.isnumeric():
#         if number[0] + number[1] + number[2] == number[3] + number[4] + number[5]:
#             print('lucky')
#             return True
#         else:
#             print("Not lucky")
#             return False
#     else:
#         print('You input not 6 numbers, or not 6 digits.')
#
# print(lucky_number('23123'))

def lucky_num(a):#str
    a = str(a)
    if a.isnumeric():
        a = int(a)
        n1 = (a) // 100000
        n2 = ((a) // 10000) % 10
        n3 = ((a) // 1000) % 10
        n4 = ((a) // 100) % 10
        n5 = ((a) // 10) % 10
        n6 = ((a) // 1) % 10
        if n1 + n2 + n3 == n4 + n5 + n6:
            print("Your number is lucky!")
            return True
        else:
            print("Your number is unlucky!")
            return False
    else:
        print("Error")

print(lucky_num('123456'))