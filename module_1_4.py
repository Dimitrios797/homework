# module_1_4.py

my_string = input("Введите текст: ")

# Вывод количества символов
print("Количество символов:", len(my_string))

# Верхний регистр
print("Верхний регистр:", my_string.upper())

# Нижний регистр
print("Нижний регистр:", my_string.lower())

# Удаление пробелов
my_string_no_spaces = my_string.replace(" ", "")
print("Без пробелов:", my_string_no_spaces)

# Первый символ
print("Первый символ:", my_string[0])

# Последний символ
print("Последний символ:", my_string[-1])
