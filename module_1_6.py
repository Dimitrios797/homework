# 2. Работа со словарями
my_dict = {"Vasya": 1975, "Egor": 1999, "Masha": 2002}

print("Dict:", my_dict)

print("Existing value:", my_dict["Masha"])  # Доступ к существующему ключу

# Доступ к отсутствующему ключу (обработка ошибки)
print("Not existing value:", my_dict.get("Petya"))  # Возвращает None, если ключ не найден

# Добавление новых пар
my_dict["Kamila"] = 1981
my_dict["Artem"] = 1915

# Удаление пары и вывод значения
deleted_value = my_dict.pop("Egor")
print("Deleted value:", deleted_value)

print("Modified dictionary:", my_dict)


# 3. Работа с множествами
my_set = {1, 'Яблоко', 42.314, 'Яблоко', 1, 1, 1}

print("Set:", my_set)  # Вывод уникальных значений

# Добавление элементов
my_set.add(13)
my_set.add((5, 6, 1.6))

# Удаление элемента
my_set.remove(1)

print("Modified set:", my_set)
