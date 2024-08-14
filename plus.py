grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Создаем пустой словарь для хранения средних баллов
average_grades = {}

# Преобразуем множество students в упорядоченный список для соответствия с grades
students_list = list(students)
students_list.sort()  # Сортируем список студентов по алфавиту

# Итерируем по спискам оценок и именам студентов
for i, student in enumerate(students_list):
  # Вычисляем средний балл для текущего студента
  average_grade = sum(grades[i]) / len(grades[i])
  # Добавляем в словарь имя студента и его средний балл
  average_grades[student] = average_grade

# Выводим словарь со средними баллами
print(average_grades)
