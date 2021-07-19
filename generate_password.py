#Напишите программу, которая с помощью модуля random генерирует nn паролей длиной m символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра
# и как минимум по одной букве в верхнем и нижнем регистре.

#Формат входных данных
#На вход программе подаются два числа n и m, каждое на отдельной строке.

import random
import string
s=string.ascii_letters.replace('l','').replace('I','').replace('o','').replace('O','')
s=s+string.digits.replace('1','').replace('0','')
num=string.digits.replace('1','').replace('0','')
low=string.ascii_lowercase.replace('o','').replace('l','')
upper=string.ascii_uppercase.replace('I','').replace('O','')
def generate_password(length):
    n=''
    n+=random.choice(num)
    n+=random.choice(low)
    n+=random.choice(upper)
    for i in range(length-3):
        n+=random.choice(s)
    n=random.sample(n,len(n))
    n=''.join(n)
    return n

def generate_passwords(count, length):
    return [generate_password(length) for i in range (count)]

n, m = int(input()), int(input())

print(*generate_passwords(n,m),sep='\n')