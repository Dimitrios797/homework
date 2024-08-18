def find_password(n):
    pairs = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                pairs.append(str(i) + str(j))

    result = ''.join(pairs)
    return result


# Примеры использования
print(find_password(9))  # Выведет: 1218273645
print(find_password(11))  # Выведет: 11029384756
print(find_password(18))  # Выведет: 12151811724272163631545414513612711810