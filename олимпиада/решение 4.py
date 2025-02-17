# Python
library = {
    "Пушкин А. С.": ["Капитанская дочка", "Евгений Онегин"],
    "Булгаков М. А.": ["Мастер и Маргарита"],
    "Достоевский Ф. М.": [
        "Преступление и наказание",
        "Братья Карамазовы",
        "Бедные люди",
        "Белые ночи",
        "Идиот"
    ]
}
sorted_library = dict(sorted(library.items()))
max_author = max(sorted_library, key=lambda author: len(sorted_library[author]))
max_count = len(sorted_library[max_author])
print(max_author, max_count)