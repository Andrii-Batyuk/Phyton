# Задание 3
# Есть некоторый текст. Посчитайте в этом тексте ко-
# личество предложений и выведите на экран полученный
# результат.

# Variables
user_str = str(input("Input some string: "))
last = len(user_str)
# Count last symbols
dot_space = user_str.count(". ") + user_str.count("!") + user_str.count("?") + user_str.count("; ")
# Looking for a last dot without space
if user_str[last-1] == '.':
    dot_space += 1
# Print results
print("There are ", dot_space, "sentences.")


