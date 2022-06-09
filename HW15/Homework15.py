"""Задание 1
Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла."""
#
# file_1 = open('task1_file_1.txt', 'rt', encoding="utf-8")
# file_2 = open('task1_file_2.txt', 'rt', encoding="utf-8")
# file_1_lines = file_1.readlines()
# file_2_lines = file_2.readlines()
#
# counter_lines_1 = 1
# counter_lines_2 = 1
#
#
# # Count number of lines in files.
# for i in file_1_lines:
#     for ch in i:
#         if ch == "\n":
#             counter_lines_1 += 1
# for i in file_2_lines:
#     for ch in i:
#         if ch == "\n":
#             counter_lines_2 += 1
#
#
# # Print number of lines in files.
# print(f'\nFile 1 have {counter_lines_1} lines, and file 2 have {counter_lines_2} lines\n')
#
# # Compare number of lines
# if counter_lines_1 == counter_lines_2:
#     print('Both files has equal count of lines\n')
# else:
#     print('Both files has different count of lines!\n')
#
# # Compare lines
# if counter_lines_1 >= counter_lines_2:
#     try:
#         for index in range(counter_lines_1):
#             if file_1_lines[index] == file_2_lines[index]:
#                 print(f'Line {index+1} in both file are equal\n')
#             else:
#                 print(
#                     f'Line {index+1} in file 1 \n{file_1_lines[index]}not equal line {index+1} in file 2\n{file_2_lines[index]} ')
#     except IndexError:
#         print(f'\nThis lines are absent in file 2 !!!!\n')
#         for i in range(counter_lines_2, counter_lines_1):
#             print(f'Line{i+1}')
#             print(file_1_lines[i])
# else:
#     try:
#         for index in range(counter_lines_2):
#             if file_2_lines[index] == file_1_lines[index]:
#                 print(f'Line {index+1} in both file are equal\n')
#             else:
#                 print(
#                     f'Line {index+1} in file 2 \n{file_2_lines[index]}not equal line {index+1} in file 1\n{file_1_lines[index]} ')
#     except IndexError:
#         print(f'\nThis lines are absent in file 1 !!!!\n')
#         for i in range(counter_lines_1, counter_lines_2):
#             print(f'Line{i+1}')
#             print(file_2_lines[i])
#
#
# # print(counter_lines_1)
# # print(counter_lines_2)
# file_1.close()
# file_2.close()

"""Задание 2
Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному
файлу:
■ Количество символов;
■ Количество строк;
■ Количество гласных букв;
■ Количество согласных букв;
■ Количество цифр."""

# print('\nTask2\n')
#
# file_task_2 = open('file_task_2.txt', 'rt')
# text_task_2 = file_task_2.read()
# ch_counter = 0
# line_counter = 0
# digit_counter = 0
# vowels = ['a', 'e', 'i', 'o', 'q', 'u', 'y']
# vowels_counter = 0
# consonant_counter = 0
#
# for character in text_task_2:
#     ch_counter += 1
#     if character == '\n':
#         line_counter += 1
#     if character.isnumeric():
#         digit_counter += 1
#     if character in vowels:
#         vowels_counter += 1
#     if character not in vowels:
#         consonant_counter += 1
# file_task_2.close()
# print(
#     f'File file_task_2.txt has {ch_counter} characters, {line_counter} lines, {digit_counter} digits, {vowels_counter} vowels, {consonant_counter} consonants.')

"""Задание 3
Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл."""

#
# with open('file1_task_3.txt', 'rt',  encoding='utf8') as text_1_task_3:
#     lines_task_3 = text_1_task_3.readlines()
#     if len(lines_task_3) > 0:
#         rows_task_3 = lines_task_3[:len(lines_task_3)-1]
#
#
# with open('file2_task_3.txt', 'wt',   encoding='utf8') as text_2_task_3:
#     text_2_task_3.writelines(rows_task_3)
# text_2_task_3.close()
# text_1_task_3.close()
# # Задание 4
# # Дан текстовый файл. Найти длину самой длинной
# # строки.
#
#
# # print(max(open('file1_task_3.txt', encoding='utf-8'), key=len))
#
# max_len_line = 0
# max_line = ''
#
# file_task_4 = open('file1_task_3.txt', encoding='utf-8')
# for lines_tsk3 in file_task_4:
#     if len(lines_tsk3) > max_len_line:
#         max_len_line = len(lines_tsk3)
#         max_line = lines_tsk3
#
# print(f'\nLongest line in file1_task_3.txt is :\n{max_line}and length is {len(max_line)} characters')
# file_task_4.close()

"""Задание 5
Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово."""
#
# count_search_word = 0
# with open('file_task_6.txt', 'rt') as file_task_5:
#     text_task_5 = file_task_5.read()
#     search_word = input("Type word in english to search: ")
#     for list_5 in text_task_5.split():
#         if list_5 == search_word:
#             count_search_word += 1


print(f'\nThe word "{search_word}" occures in text {count_search_word} times.')

"""Задание 6
Дан текстовый файл. Найти и заменить в нем задан-
ное слово. Что искать и на что заменять определяется
пользователем."""

#
# word_to_find = input("Write word to find: ")
# word_to_replace = input("Write word to replace: ")
# with open('file_task_6.txt', 'rt') as file6:
#     data6 = file6.read()
#     data6 = data6.replace(word_to_find, word_to_replace)
# with open('file_task_6.txt', 'wt') as file6:
#     file6.write(data6)
