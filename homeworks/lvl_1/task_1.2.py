# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

from random import randint

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

sum = 0 # общая сумма времени
sum_min = 0
sum_sec = 0
sum_sec2 = 0

for j in range(3): # цикл для количества отслеживаемых песен
    n = randint(0, len(my_favorite_songs)) # рандомное число в пределах количества треков
    for i in my_favorite_songs:
            if my_favorite_songs.index(i) == n: # если индекс трека равен рандомному числу...
                  print ('Случайная мелодия №', n+1, i) # вывод названия трека
                  sum = sum + i[1] #добавление его времени в сумму
                  sum_min = sum_min + i[1] // 1 # подсчёт суммы минут
                  sum_sec = sum_sec + i[1] % 1 # подсчёт суммы секунд
sum_sec2 = ((sum_sec // 1 * 100) / 60 + sum_sec % 1) # пересчёт суммы секунд из 10-й системы в 60-ю

print ('Вариант 1: Три песни звучат', int(sum//1),'минут') # вывод суммы времени в минутах
print ('Вариант 2: Три песни звучат', int(sum_min//1 + sum_sec2 // 60),'минут и ', int((sum_sec2 * 100) % 60), 'секунд') # вывод суммы времени в минутах и секундах

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

