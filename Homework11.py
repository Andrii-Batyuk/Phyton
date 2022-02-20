"""Задание 1: Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12. Необходимо вывести на экран
результат выражения. В нашем примере это 35. Арифметическое выражение может состоять только из трёх частей: число,
операция, число. Возможные операции: +, -,*,/ """

#Variables
a = str(input("Input some impression: "))
operators = ['+', '-', '*', '/']
operator = 0
operator_index = 0
# Cycle for enumerating type of operator
for i in a:
    for b in operators:
        if b == i:
            operator = b
            break
# Enumerating operator's index
operator_index = a.index(operator)
# Calculating and printing results
if operator == "+":
    print(int(a[:operator_index]) + int(a[operator_index+1:]))
elif operator == "-":
    print(int(a[:operator_index]) - int(a[operator_index+1:]))
elif operator == "*":
    print(int(a[:operator_index]) * int(a[operator_index+1:]))
elif operator == "/":
    print(int(a[:operator_index]) / int(a[operator_index+1:]))
else:
    print("You input something wrong! ")