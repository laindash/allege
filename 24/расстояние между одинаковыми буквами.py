# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
a = open('file.txt').readlines()
s = []
c = 0
for i in a:
    if i.count('A') < 25:
        for d in range(len(i)):
            r = i.rfind(i[d]) - i.find(i[d])
            s.append(r)
print(max(s))

