# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых не более одной буквы A.
a = open("file.txt").readline()
count = count_old = m = 0
for i in a:
    if i == "A":
        m = max(m, count + count_old - 1)
        count_old = count
        count = 0
    count += 1
print(m)
