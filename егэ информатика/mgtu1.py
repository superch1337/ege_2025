# Чтение входных данных
N, K = map(int, input().split())
unique_recipes = set()

# Чтение рецептов
for _ in range(N):
    recipe = tuple(sorted(map(int, input().split()))[1:])  # Сортируем и убираем количество
    unique_recipes.add(recipe)

# Ответ - количество уникальных рецептов
print(len(unique_recipes))