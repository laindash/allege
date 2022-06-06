# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
a = open('file.txt').readline()
s = []
for i in range(len(a) - 2):
    if a[i] == a[i + 1]:
        s.append(a[i + 2])
o = set()
for i in s:
    o.add(i)
t = []
for i in o:
    y = s.count(i), i
    t.append(y)
print(max(t))
