# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.

x = 100
y = 999

for i in range(x, y+1):
    i = str(i)
    if i[0] == i[1] or i[0] == i[2] or i[1] == i[2]:
        print(i)