def calculate_structure_sum(data):
    total_sum = 0

    # Проверяем тип данных и обрабатываем соответственно
    if isinstance(data, list):
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для каждого элемента списка
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Суммируем длину ключа
            total_sum += calculate_structure_sum(value)  # Рекурсивный вызов для значения
    elif isinstance(data, tuple):
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для каждого элемента кортежа
    elif isinstance(data, str):
        total_sum += len(data)  # Суммируем длину строки
    elif isinstance(data, (int, float)):
        total_sum += data  # Суммируем число

    return total_sum


# Пример использования функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99