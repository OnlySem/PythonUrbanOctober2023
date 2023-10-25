def averege_population (cities):
    return sum([population["population"] for population in city_list])/len(city_list)

city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

# num_cities = len(city_list)  # TODO найдите количество городов в списке

'''Поиск общего числа населения городов с помощью цикла for'''
# total_population=0
# for i in range(num_cities):
#     total_population += city_list[i]["population"]  # TODO найдите общее количество населения




print(f"Среднее арифметическое населения равно = {averege_population(city_list)}")  # TODO распечатайте среднее арифметическое населения
