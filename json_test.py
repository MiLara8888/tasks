# К вам в руки попал файлик формата json ,
# в котором содержится информация одного автосалона о продажах менеджеров.
# В файле указано для каждого менеджера список проданных им автомобилей,
# а также проставлена цена продажи каждого автомобиля.
# Вывести сводку по колличеству проданных машин и по итоговым продажам
import json

n = ''
with open('manager_sales (1).json', 'r', encoding='utf8') as file:
    n = json.load(file)
dic = {}
for i in n:
    print('manager', i['manager']['first_name'], i['manager']['last_name'], 'sold -', len(i['cars']))
    summ = 0
    k = i['cars']
    for i in k:
        summ += int(i['price'])
    print('for total cost -', summ)
    print('--------------')
