#1
"""
Есть список преобразовать названия в списке в нижний регистр
применяя искл функцию map, если хотите можете применить
lambda функцию тоже, но можно и без нее
"""

cities = ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN', 'ANKARA', 'AMSTERDAM']

def make_to_lower(city_name):
    return city_name.lower()

#первый способ
cities_lower = list(map(make_to_lower, cities))

#второй способ
cities_lower = list(map(lambda city_name: city_name.lower(), cities))

print(cities_lower)

