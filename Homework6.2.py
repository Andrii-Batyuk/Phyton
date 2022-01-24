#Python Home Work 6.2
# Пользователь вводит с клавиатуры количество ме-
# тров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

metr = float(input("Input distance in meters: "))
oper = int(input("Convert in miles type 1, inches type 2, yards type 3: "))
if  oper != 1 and oper != 2 and oper != 3:
    print("You type something wrong, try again.")
elif oper == 1:
    print(metr, "meters are", metr * 0.000621371,"miles.")
elif oper == 2:
    print(metr, "meters are", metr * 39.37,"inches.")
elif oper == 3:
    print(metr, "meters are", metr * 1.09361, "yards.")
else:
    print("You type something wrong, try again.")