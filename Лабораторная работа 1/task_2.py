def number_cities(cities, max_population=5):
    return len([population for population in cities if population['population'] < max_population])

city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

# max_population = 5  # Пороговое значение для населения
# num_cities=0
# for i in range(len(city_list)):
#     if city_list[i]["population"]<5:
#         num_cities += 1  # TODO найдите количество городов с населением меньшн 5 млн.

print(f"Количество городов с население до 5 млн. жителей равно = {number_cities(city_list)}")
