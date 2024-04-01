#1
"""
Есть список преобразовать названия в списке в нижний регистр
применяя искл функцию map, если хотите можете применить
lambda функцию тоже, но можно и без нее
"""

# cities = ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN', 'ANKARA', 'AMSTERDAM']

# def make_to_lower(city_name):
#     return city_name.lower()

# #первый способ
# cities_lower = list(map(make_to_lower, cities))

# #второй способ
# cities_lower = list(map(lambda city_name: city_name.lower(), cities))

# print(cities_lower)

#2
"""
Отфильтруйте отобрав в новый список только четные числа
и возведите в третью степень каждую цифру отфильтрованного
списка
"""

# numbers = [4, 3, 6, 8, 9, 7, 1, 2, 34, 5, 56, 76]

# numbers = list(filter(lambda x: x % 2 ==0, numbers))
# numbers = list(map(lambda x: pow(x, 3), numbers))

# print(numbers)

#3
"""
Вычислите сумму элементов списка, но перед этим отфильтровать
только нечетные числа
"""

# from functools import reduce

# numbers = [34, 5, 23, 68, 56, 890, 123, 564]
# numbers = reduce(lambda x, y: x + y, filter(lambda x: x % 2 != 0, numbers))

# print(numbers)

#4
"""
Удвоение чисел в списке: пусть дан список чисел
удвоить каждое число в списке, исп map
"""

# from random import randint

# numbers = [randint(1, 101) for x in range(1, 20)]
# print(numbers)

# numbers = list(map(lambda x: x * 2, numbers))
# print(numbers)

#5
"""
Найти сумму квадратов чисел в списке, используя reduce
"""

# from random import randint
# from functools import reduce

# numbers = [randint(1, 3) for x in range(1, 5)]
# print(numbers)

# result = reduce(lambda x, y: x + y**2, numbers)
# print(result)

#6
"""
Отфильтровать слова по длине. Только те строки,
которые имеют длину больше 5 символов, используя filter
"""

# strings = ['apple', 'banana', 'cherry', 'grape', 'watermelon']

# print(list(filter(lambda x: len(x) > 5, strings)))

#7
"""
Найти произведение элементов списка, use reduce
"""

# from random import randint
# from functools import reduce

# numbers = [randint(1, 10) for x in range(1, 5)]
# print(numbers)
# print(reduce(lambda x, y: x * y, numbers))

#8
"""
Оставить только положительные числа в списке
используя filter
"""

# from random import randint

# numbers = [randint(-10, 10) for x in range(1, 10)]
# print(numbers)

# print(list(filter(lambda x: x > 0, numbers)))

