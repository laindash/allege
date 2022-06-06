# определите максимальное количество идущих подряд символов, где два соседних различны
with open('file.txt') as f:
    s = f.readline()
    k = 1
    kmax = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            k += 1
            kmax = max(kmax, k)
        else:
            k = 1
print(kmax)
