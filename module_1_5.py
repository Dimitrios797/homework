# module_1_5.py

# 1. Неизменяемый кортеж
immutable_var = (1, 2, 'a', 'b')

# Вывод кортежа
print("Immutable tuple:", immutable_var)

# Попытка изменить элемент кортежа
# immutable_var[0] = 10 # Вызовет ошибку!

# Объяснение:
# Кортежи в Python неизменяемы, поэтому нельзя напрямую изменять их элементы.
# Попытка присвоить новое значение элементу кортежа вызовет ошибку TypeError.

# 2. Изменяемый список
mutable_list = [1, 2, 'a', 'b']

# Изменение элемента списка
mutable_list[4] = 'Modified' # Добавляем новый элемент

# Вывод измененного списка
print("Mutable list:", mutable_list)