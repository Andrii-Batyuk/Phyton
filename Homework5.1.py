#Python Home Work 5
# Написать программу, которая по выбору пользователя
# возводит введенное им число в степень от нулевой
# до седьмой включительно.

num = int(input("Input some value to calculate: "))
step = 0

if num == 0:
    print("Error! You type", num)
else:
    # First solution:
    print(num**0, num**1, num**2, num**3, num**4, num**5, num**6, num**7)

# Second solution:
while step < 8:
    print(num ** step, end=" ")
    step = step + 1