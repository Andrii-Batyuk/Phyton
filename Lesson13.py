#Strings

#
# h = 'Hello, World!'
# #    0123456789
# print(h)
# print(h[0])
# print(h[1])
# print(h[2])
# print(h[3])

# n = 'Andrii Batyuk'
# #    0123456789
#
#
# print(n[0], n[3], n[9], n[6], n[0], n[1], n[2], n[6], n[7], n[0], n[1], n[0], n[1], n[0]) # Art

# s = 'Hello, World'
# rs = ''

# for i in range(len(s)):
#     rs = s[i] + rs
# print(rs)

#
# s = 'Hello, World'
# for i in range(1, len(s)+1):
#     print(s[-i])


# Задание 2
# Пользователь вводит с клавиатуры строку. Посчитайте количество букв,
# цифр в строке. Выведите оба
# количества на экран.'''


#
# letters = 'abcdefghijklmnopqrstuvwxyz '
# numbers = '01234567890'
#
# s = 'hello123asdoifodifsio asdfhwkerwer 87678yiuh lkjkhw87jbkn 9o86yh3k4jn3jkb4hfjksadhfis6ad989f689asadfhoasd89f72803u5oijs[oiuasdoi[njtr9089v33745vnetjmnr986y7yr98wer'
# count_numbers = 0
# count_letters = 0

# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letters = count_letters + 1
#     for l in range(len(numbers)):
#         if a == numbers[l]:
#             count_numbers = count_numbers + 1
# print()
# print(count_letters, count_numbers)

# s = 'hello123asdoifodifsio asdfhwkerwer 87678yiuh lkjkhw87jbkn 9o86yh3k4jn3jkb4hfjksadhfis6ad989f689asadfhoasd89f72803u5oijs[oiuasdoi[njtr9089v33745vnetjmnr986y7yr98wer'
# # number = '9'
# # print(number.isnumeric())
# # print(number.isalpha())
#
# count_numbers = 0
# count_letters = 0
# letters = 'abcdefghijklmnopqrstuvwxyz '
# numbers = '01234567890'
#
# for i in range(len(s)):
#     a = s[i]
#     for l in range(len(letters)):
#         if a.isalpha():
#             count_letters = count_letters + 1
#     for m in range(len(numbers)):
#         if a.isnumeric():
#             count_numbers = count_numbers + 1
# print()
# print(count_letters, count_numbers)

s = 'Abram Kadabram'
symbol = 'a'
count = 0
# for i in s:
#     if i == symbol:
#         count = count + 1
# print(count)
#
# print(count)
print(s.count(symbol))