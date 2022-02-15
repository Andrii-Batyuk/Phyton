# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

x = 100
y = 9999

for i in range(x, y+1):
    i = str(i)
    if int(i) < 999:
        if i[0] != i[1] and i[0] != i[2] and i[1] != i[2]:
            print(i)
    if int(i) > 999:
        if i[0] != i[1] and i[0] != i[2] and i[1] != i[2] and i[0] != i[3] and i[1] != i[3] and i[2] != i[3]:
            print(i)