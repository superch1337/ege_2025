from datetime import datetime, timedelta


# Вспомогательные функции
def parse_time(time_str):
    """Парсинг времени в формате h:mm в datetime."""
    return datetime.strptime(time_str, "%H:%M")


def calculate_training_time(start, end, treadmill, bike):
    """Эмуляция тренировок на беговой дорожке и велотренажёре."""
    treadmill_time, bike_time = 0, 0
    treadmill_ready, bike_ready = True, True  # Готовность тренажёров
    treadmill_cooldown, bike_cooldown = None, None  # Время до окончания отдыха тренажёров

    current_time = start
    while current_time < end:
        if treadmill_ready:  # Если беговая дорожка готова
            train_time = min(timedelta(minutes=30), end - current_time)
            treadmill_time += train_time.seconds // 60
            current_time += train_time
            treadmill_ready = False
            treadmill_cooldown = current_time + timedelta(minutes=20)
        elif bike_ready:  # Если велотренажёр готов
            train_time = min(timedelta(minutes=20), end - current_time)
            bike_time += train_time.seconds // 60
            current_time += train_time
            bike_ready = False
            bike_cooldown = current_time + timedelta(minutes=30)
        else:  # Если оба тренажёра на отдыхе, ждём ближайшего готового
            next_ready = min(treadmill_cooldown, bike_cooldown)
            current_time = next_ready
            if current_time == treadmill_cooldown:
                treadmill_ready = True
            if current_time == bike_cooldown:
                bike_ready = True

    return treadmill_time, bike_time


# Данные задачи
N = 3
busy_intervals = [
    "9:12-9:20",
    "11:30-12:10",
    "15:00-15:45"
]

# Константы
WORK_START = parse_time("9:00")
WORK_END = parse_time("18:00")

# Парсинг занятых промежутков
busy_times = [(parse_time(start), parse_time(end)) for interval in busy_intervals for start, end in
              [interval.split("-")]]

# Вычисление свободных промежутков
free_intervals = []
current_start = WORK_START
for busy_start, busy_end in busy_times:
    if current_start < busy_start:
        free_intervals.append((current_start, busy_start))
    current_start = busy_end
if current_start < WORK_END:
    free_intervals.append((current_start, WORK_END))

# Эмуляция тренировок по свободным промежуткам
total_treadmill_time, total_bike_time = 0, 0
for free_start, free_end in free_intervals:
    treadmill_time, bike_time = calculate_training_time(free_start, free_end, treadmill=True, bike=True)
    total_treadmill_time += treadmill_time
    total_bike_time += bike_time

total_treadmill_time, total_bike_time