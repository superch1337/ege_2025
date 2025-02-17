def parse_input():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    # Размеры поля и точка входа
    N, M, K = map(int, data[0].split())

    # Поле
    field = [list(map(int, data[i + 1].split())) for i in range(N)]

    # Метки-направления
    P = int(data[N + 1])
    directions = {}
    for i in range(P):
        direction, row, col = map(int, data[N + 2 + i].split(";"))
        directions[(row - 1, col - 1)] = direction

    return N, M, K - 1, field, directions


def simulate_robot(N, M, K, field, directions):
    visited = set()  # Хранит посещенные ячейки
    x, y = N - 1, K  # Начальная позиция (снизу)
    time_spent = 0

    while 0 <= x < N and 0 <= y < M:
        if (x, y) in visited:  # Если робот застрял
            return f"{x + 1} {y + 1}\n{time_spent}"

        visited.add((x, y))  # Добавляем текущую клетку в посещенные
        time_spent += field[x][y]  # Увеличиваем общее время

        # Проверяем метку
        if (x, y) in directions:
            direction = directions[(x, y)]
            if direction == 1:  # "Зеркало 1" – отражение
                x, y = x - 1, y - 1
            elif direction == 2:  # "Зеркало 2" – отражение
                x, y = x - 1, y + 1
        else:
            # Без метки робот движется вверх
            x -= 1

    # Если робот выехал за границы
    return f"0\n{time_spent}"


def main():
    N, M, K, field, directions = parse_input()
    result = simulate_robot(N, M, K, field, directions)
    print(result)


if name == "__main__":
    main()