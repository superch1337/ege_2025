def calculate_distance(L, K, U, obstacles, doors):
    # Упорядочим препятствия и двери по координатам
    obstacles.sort(key=lambda x: x[0])
    doors = set(doors)

    # Моделирование движения
    position = 0
    while position < L:
        # Проверяем препятствия в пределах радиуса стрельбы
        for i, (coord, hp) in enumerate(obstacles):
            if coord < position - K:
                continue  # Препятствие вне радиуса стрельбы
            if coord > position + K:
                break  # Препятствие дальше радиуса стрельбы

            # Проверяем, есть ли дверь между персонажем и препятствием
            if any(position <= door <= coord for door in doors):
                continue  # Дверь блокирует стрельбу

            # Стреляем в препятствие
            obstacles[i] = (coord, hp - U)
            if obstacles[i][1] <= 0:
                obstacles.pop(i)  # Препятствие уничтожено
                break
            else:
                return coord  # Не успели уничтожить, игра заканчивается

        # Перемещаемся на следующую позицию
        position += 1

    return L  # Если дошли до конца


# Ввод данных
L, K, U = map(int, input().split())
N = int(input())
obstacles = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
doors = [int(input()) for _ in range(M)]

# Вывод результата
print(calculate_distance(L, K, U, obstacles, doors))