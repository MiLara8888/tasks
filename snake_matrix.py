#Заполнить матрицу змейкой №1
n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
chiclo=1
for i in range (n):
    if i%2==0:
        for j in range(n):
            a[i][j]=chiclo
            chiclo+=1
    elif i%2!=0:
        for j in range(n-1,-1,-1):
            a[i][j] = chiclo
            chiclo += 1
for i in a:
    print(i)



