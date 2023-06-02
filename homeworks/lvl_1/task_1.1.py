# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
start_song=0
a = []
for i in range(len(my_favorite_songs)):
    if my_favorite_songs[i] == ',':
#        print(my_favorite_songs[start_song:i])
        a.append (my_favorite_songs[start_song:i])
        start_song = i+2
a.append (my_favorite_songs[start_song:])
print (a[0])
print (a[-1])
print (a[1])
print (a[-2])


