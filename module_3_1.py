# Глобальная переменная для подсчета вызовов
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим строку и элементы списка к нижнему регистру для сравнения
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

# Примеры вызовов функций
print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False

# Выводим количество вызовов
print(calls)  # 4