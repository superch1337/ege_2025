MODULO = 10**9 + 7

def power_of_two(p, modulo=MODULO):
    """Возвращает 2^p по модулю MODULO."""
    return pow(2, p, modulo)

def maximize_result(array, k):
    """Максимизирует результат sum + x * k для заданного массива."""
    sum_units = 0
    zero_segments = 0
    in_zero_segment = False

    for num in array:
        if num >= 0:
            sum_units = (sum_units + num) % MODULO
            in_zero_segment = False
        else:
            if not in_zero_segment:
                zero_segments += 1
                in_zero_segment = True

    result = (sum_units + zero_segments * k) % MODULO
    return result

# Чтение входных данных
t = int(input())
for _ in range(t):
    n = int(input())
    array = []
    for _ in range(n):
        sign, p = input().split()
        p = int(p)
        a_i = power_of_two(p) if sign == '+' else -power_of_two(p)
        array.append(a_i)

    # Чтение и вычисление k
    sign_k, p_k = input().split()
    p_k = int(p_k)
    k = power_of_two(p_k) if sign_k == '+' else -power_of_two(p_k)

    # Вычисление и вывод результата
    result = maximize_result(array, k)
    print(result)