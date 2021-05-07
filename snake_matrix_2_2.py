n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
number, x, y = 1, 0, n - 1
count = int(n / 2)


def rotate_matrix(m):  # функция разворота матрицы
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]


while count != 0:
    iter = 4
    while iter != 0:
        for i in range(x, y):
            a[x][i] = number
            number += 1
        a = rotate_matrix(a)
        iter -= 1
    count -= 1
    x += 1
    y -= 1

if n % 2 != 0:
    a[x][y] = n ** 2

for i in a:
    print(*i)
