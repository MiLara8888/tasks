# Дано слово ТАРАКАНИЩЕ
# какое максимальное количество 6-буквенных слов можно составить из букв данного слова, если
# 1) начинается с согласной
# 2) согл и гл чередуются
# 3) буквы не повторяются

n='ТАРАКАНИЩЕ'
sogl='ТРКНЩ'
gl='АИЕ'
l=set()
for a in n:
    if a not in sogl:
        continue
    for b in n:
        if b not in gl:
            continue
        for c in n:
            if c not in sogl:
                continue
            for d in n:
                if d not in gl:
                    continue
                for e in n:
                    if e not in sogl:
                        continue
                    for f in n:
                        if f not in gl:
                            continue
                        if len(set(a+b+c+d+e+f))==6:
                            l.add(a+b+c+d+e+f)
print(len(l))



