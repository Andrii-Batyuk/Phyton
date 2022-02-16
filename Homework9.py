# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеариф-
# метическое каждой группы.

x = int(input("Input first number: "))
y = int(input("Input second number: "))
sumeven = 0
sumodd = 0
sumnine = 0
countereven = 0
counterodd = 0
counternine = 0
for i in range(x, y+1):
    if i % 2 == 0:
        sumeven = sumeven + i
        countereven = countereven + 1
    if i % 2 != 0:
        sumodd = sumodd + i
        counterodd = counterodd + 1
    if i > 8 and i % 9 == 0:
        sumnine = sumnine + i
        counternine = counternine + 1
print("Sum of even numbers:", sumeven)
print("Arithmetic mean of even numbers:", sumeven // countereven)
print("Sum of odd numbers:", sumodd)
print("Arithmetic mean of odd numbers:", sumodd // counterodd)
print("Sum of numbers equal 9:", sumnine)
if sumnine < 9:
    print("Arithmetic mean of numbers equal 9:", 0)
else:
    print("Arithmetic mean of numbers equal 9:", sumnine // counternine)
