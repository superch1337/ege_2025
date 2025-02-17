from datetime import datetime, timedelta


def parse_time_interval(interval):
    start, end = interval.split('-')
    return datetime.strptime(start, "%H:%M"), datetime.strptime(end, "%H:%M")


def calculate_schedule(teachers):
    all_options = []
    for lectures in teachers:
        options = []
        for lecture in lectures:
            start, end = parse_time_interval(lecture)
            options.append((start, end))
        all_options.append(options)

    from itertools import product
    min_wait_time = float('inf')
    best_schedule = None

    # Перебираем все комбинации лекций (по одной от каждого преподавателя)
    for combination in product(*all_options):
        sorted_combination = sorted(combination, key=lambda x: x[0])
        wait_time = 0
        total_time = 0
        start_first = sorted_combination[0][0]

        for i in range(len(sorted_combination)):
            start, end = sorted_combination[i]
            total_time += (end - start).seconds // 60
            if i > 0:
                prev_end = sorted_combination[i - 1][1]
                wait_time += max(0, (start - prev_end).seconds // 60)

        if wait_time < min_wait_time or (wait_time == min_wait_time and start_first < best_schedule[0][0]):
            min_wait_time = wait_time
            best_schedule = sorted_combination

    first_start = best_schedule[0][0].strftime("%H:%M")
    return first_start, total_time, min_wait_time


# Чтение входных данных
n = int(input())
teachers = []
for _ in range(n):
    n_i = int(input())
    lectures = [input().strip() for _ in range(n_i)]
    teachers.append(lectures)

# Решение задачи
first_start, total_time, wait_time = calculate_schedule(teachers)

# Вывод результатов
print(first_start)
print(total_time)
print(wait_time)