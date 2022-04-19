# максимальное кол-во подряд идущих пар AC или AB. Подстрока может содержать только АВ или АС, или одновременно обе пары
s = open('file.txt').readline()
s = s.replace('AC', 'X')
s = s.replace('AB', 'X')
count = 0
m = 0
for i in range(len(s)):
    if s[i] == 'X':
        count += 1
        m = max(count, m)
    else:
        count = 0
print(m)
