#Lesson 14

# '''Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран.
# * Без использования метода count'''
# s = 'Abrakadabra'
# symbol = 'ra'
# print(s.count(symbol))
# '''Задание 5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.
# * Без использования метода replace'''
# s = 'Abrakadabra'
# symbol = 'ra'
# new_symbol = 'RA'
# print(s.replace(symbol,new_symbol))
#
# print(s)

# Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран

# string = str(input("Type some string: "))
# search = str(input("Type search word"))
#
# for i in string:
#     if sear

# '''Задание 1
# Есть некоторый текст. Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось
# с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в
# тексте.'''


# t = 'some interesting, text and else. what i am doing.how do you do? i am fine! thank you.'
# t = t.capitalize()
# symbols = '!.?'
# for i in range(len(t)):
#     for s in range(len(symbols)):
#         if t[i]
#
#
#
#             number = '0123456789'
#             spe = '!?,.'
#             s = 'some interesting, text and else! what i am doing. how do you do? i am fine! thank you.'
#             count_number = 0
#             count_symbol = 0
#             count_spe = 0
#             count_spea = 0
#             for i in range(len(s)):
#                 print(s[i])
#                 a = s[i]
#
#                 if a in number:
#                     count_number = count_number + 1
#                 if a in spe:
#                     count_spe = count_spe + 1
#                 if a == spe[0]:
#                     count_spea = count_spea + 1
#             print(count_symbol, count_number, count_spe, count_spea)


largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02