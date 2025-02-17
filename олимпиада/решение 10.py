# Python
def calculate_min_time():

    n = int(input().strip())

    food_amounts = list(map(float, input().strip().split()))

    eating_speeds = list(map(float, input().strip().split()))

    food_amounts.sort(reverse=True)
    eating_speeds.sort()

    times = [food / speed for food, speed in zip(food_amounts, eating_speeds)]

    min_time = max(times)

    print(f"{min_time:.2f}")
calculate_min_time()
