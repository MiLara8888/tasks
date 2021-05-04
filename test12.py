#Реализуйте программу, которая будет эмулировать работу с пространствами имен.
# Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
# Вашей программе на вход подаются следующие запросы:
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>,
# или None, если такого пространства не существует

n = int(input())
dic = {'global': ['global']}


def geter(namesp, var):
    if var in dic[namesp]:
        print(namesp)
        return
    elif namesp == 'global' and var not in dic['global']:
        print('None')
        return
    else:

        return geter(dic[namesp][0], var)


while n != 0:
    task, namespase, perem = input().split()
    if task == 'create':
        dic[namespase] = [perem]
    elif task == 'add':
        dic[namespase] += [perem]
    elif task == 'get':
        geter(namespase, perem)
    n -= 1
