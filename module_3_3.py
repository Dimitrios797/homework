def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызов функции с разным количеством аргументов
print_params()  # без аргументов
print_params(10)  # только a
print_params(10, 'текст')  # a и b
print_params(10, 'текст', False)  # все параметры
print_params(b=25)  # изменение только b
print_params(c=[1, 2, 3])  # изменение только c

# Создание списка и словаря
values_list = [3.14, 'пример', False]
values_dict = {'a': 42, 'b': 'слово', 'c': None}

# Распаковка параметров
print_params(*values_list)  # распаковка списка
print_params(**values_dict)  # распаковка словаря

# Создание второго списка
values_list_2 = [54.32, 'Строка']

# Вызов функции с распаковкой и дополнительным параметром
print_params(*values_list_2, 42)  # распаковка списка и передача 42