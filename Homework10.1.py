# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.

# Variables
user_str = str(input("Input some text: "))
user_word = input("Input worlds to change in uppercase: ")
# Converting string in lowercase
user_str = user_str.lower()
# Creating list
user_word = user_word.split()
# Cycle to change words in uppercase
for i in user_word:
    user_str = user_str.replace(i.lower(), i.upper())
# Displaying results
print(user_str)

# Some text to change. Let's try to convert it!

