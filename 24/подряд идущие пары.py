# максимальное кол-во подряд идущих пар AC или AB. Подстрока может содержать только АВ или АС, или одновременно обе пары
a = open('file.txt').readline()
a = a.replace('AC', 'X')
a = a.replace('AB', 'X')
c = 0
s = []
for i in a:
    if i == '*':
        c += 1
    else:
        s.append(c)
        c = 0
print(max(s))
