from random import randint

class Matrix:
    def __init__(self, n, m):
        self._matrix = [
            [None for i in range(m)]
            for j in range(n)
            ]
        self.rows = n
        self.columns = m
        
    def get_rows(self):
        return self.rows
    
    def get_columns(self):
        return self.columns

    def set_value(self, n, m, a):
        a = randint(1, p+1)
        if a == p+1:
            a = 'None'
        self._matrix[n][m] = a
    
    def get_value(self, n, m):
        return self.matrix[n][m]

m = int(input ('Введите количество строк матрицы: '))
n = int(input ('Введите количество столбцов матрицы: '))
p = int(input ('Введите предел чисел для матрицы: '))
m = Matrix(m, n)

for i in range(m.get_rows()):
    for j in range(m.get_columns()):
        m.set_value(i, j, 1)

print('Классический вид матрицы:')
for i in m._matrix:
    print (i, end = '\n')
    
print('Строчный вид матрицы:')
print(m._matrix)