#Робот расположен в точке 0:0 , робот движется по спирали в следующем порядке
# (0:0),(-1:0),(-1:-1),(0:-1),(1:-1),(1:0),(1:1),(0:1),(-1:1),(-2:-1)
#определить где будет находиться робот через N шагов


k = 1
x = 0
m = [[0, 0]]
l = int(input())
flag = True
while flag:
    if len(m) == 1 and l == 0:
        print(*m[-1])
        flag = False

    if flag==False:
        break
    for i in range(k - 1, (-k) - 1, -1):
        m.append([-k, i])
        if len(m) - 1 == l:
            print(*m[-1])
            flag = False
            break
    if flag==False:
        break
    for i in range(x, k + 1):
        m.append([i, -k])
        if len(m) - 1 == l:
            print(*m[-1])
            flag = False
            break
    if flag==False:
        break
    for i in range(x, k + 1):
        m.append([k, i])
        if len(m) - 1 == l:
            print(*m[-1])
            flag = False
            break
    if flag==False:
        break
    for i in range(k - 1, x - 2, -1):
        m.append([i, k])
        if len(m) - 1 == l:
            print(*m[-1])
            flag = False
            break
    if flag==False:
        break
    k += 1
    x -= 1
