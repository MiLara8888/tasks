#Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными,
# состоящая из строчных букв и цифр, и если в ней присутствует слово "anton"
# (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число nn – количество холодильников.
# В последующих nn строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 55 до 100100 символов.
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.
#
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
#
# 1 2 3
# Sample Input 2:
#
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
#
# 1 2 7 8

ant = 'anton'
for i in range(int(input())):
    ant_ind = 0  # бежит по буквам слова антон
    for j in (input()):
        if j in ant[ant_ind] and ant_ind != 5:  # проверят последовательно на строчке совпадения
            ant_ind += 1
        if ant_ind == 5:
            break
    if ant_ind == 5:
        print(i + 1, end=' ')