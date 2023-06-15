# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

a = [4,6,2,1,9,63,-134,566]
b = [-52, 56, 30, 29, -54, 0, -110]
c = [42, 54, 65, 87, 0]
d = [5]

def minimum(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min

def maximum(a):
    max = a[0]
    for i in a:
        if i > max:
            max = i
    return max 

print(a, '     -> max = ',maximum(a), ', min = ', minimum(a))
print(b, '     -> max = ',maximum(b), ', min = ', minimum(b))
print(c, '     -> max = ',maximum(c), ', min = ', minimum(c))
print(d, '     -> max = ',maximum(d), ', min = ', minimum(d))
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
