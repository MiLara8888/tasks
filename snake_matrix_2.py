# Заполнить матрицу змейкой №2
n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
number, x, y = 1, 0, n - 1
count = int(n / 2)
while count != 0:
    for i in range(x, y):  # горизонталь вправо
        a[x][i] = number
        number += 1
    for i in range(x, y):  # вертикаль вниз
        a[i][y] = number
        number += 1
    for i in range(y, x, -1):  # горизонталь влево
        a[y][i] = number
        number += 1
    for i in range(y, x, -1):  # вертикаль вверх
        a[i][x] = number
        number += 1
    x += 1
    y -= 1
    count -= 1

if n % 2 != 0:
    a[x][y] = n ** 2

for i in a:
    print(*i)
