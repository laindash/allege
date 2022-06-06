# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле сразу после буквы A.
a = open('file.txt').readline().strip()
s = a.split('A')
t = []
for i in s:
    t.append(i[:1])
o = set()
d = []
for i in t:
    if i not in o:
        y = t.count(i), i
        d.append(y)
        o.add(i)
    else:
        continue
print(max(d))
