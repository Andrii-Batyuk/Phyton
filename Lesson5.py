#And, Or, Not
# a = 2
# b = 3
# c = 4
# if a == b == c:
#     print(3)
# elif b == c:
#     print(2)
# elif a == c:
#     print(2)
# elif a == b:
#     print(2)
# else:
#     print("No equals")


# x = -2
# y = 0
#
# if x == 0:
#     if y == 0:
#         print("Your values is 0 0 so your dot in the center of coordinates, try to type another values!")
# if x > 1:
#     if y > 1:
#         print(1)
# if x <= 0:
#     if y > 1:
#         print(2)
# if x >= 0:
#     if y < 1:
#         print(3)
# if x < 0:
#     if y < 0:
#         print(4)
# if x == 0:
#     if y >= 0:
#         print("The dot lays in a X axis")
# if x == 0:
#     if y <= 0:
#         print("The dot lays in a X axis")
# if x >= 0:
#     if y == 0:
#         print("The dot lays in a Y axis")
# if x <= 0:
#     if y == 0:
#         print("The dot lays in a Y axis")

# a = 2
# b = 2
# c = 2
# if a == b and b == c:
#     print(3)
# elif a==b or a ==c or b ==c:
#     print(2)

# x = 3
# y = -2
#
# if x == 0 and y == 0:
#         print("Your values is 0 0 so your dot in the center of coordinates, try to type another values!")
# if x >= 1 and y >= 1 and x != 0 and y != 0:
#         print(1)
# if x < 0 and y >= 1 and x != 0 and y != 0:
#          print(2)
# if x > 0 and y <= 1 and x != 0 and y != 0:
#          print(3)
#  if x < 0 amd y < 0 and x != 0 and y != 0:
#          print(4)
#  if x == 0 and y >= 0:
#         print("The dot lays in a X axis")
# if x == 0:
#     if y <= 0:
#         print("The dot lays in a X axis")
# if x >= 0:
#     if y == 0:
#         print("The dot lays in a Y axis")
# if x <= 0:
#     if y == 0:
#         print("The dot lays in a Y axis")

# number = int(input("Please enter a number :"))
# if number == 0:
#     print("You type zero")
# elif number % 7 == 0:
#      print("The number is multiply 7")
# elif number % 7 != 0:
#    print("The number is not multiply 7")
# else:
#     print("Error")


seconds = int(input("Enter how much seconds is pass to enumerate how much time you have till midnight "))
if seconds == 0:
    print("Till midnight whole day!")
last = 86400 - seconds ;
print("till midnight", last / 60, "minutes, or", last / 60 / 60, "hours")
