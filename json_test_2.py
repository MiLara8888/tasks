import json

n = ''
with open('group_people (1).json', 'r', encoding='utf8') as file:
    n = json.load(file)

maxx, group = 0, 0
for i in n:
    k = i['people']
    count = 0
    for j in k:
        if j['year'] > 1977 and j['gender'] == 'Female':
            count += 1
    if count > maxx:
        maxx = count
        group = i['id_group']
print(maxx, group)
