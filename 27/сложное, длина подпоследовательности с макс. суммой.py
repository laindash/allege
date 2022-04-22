f = open('file.txt')
N = int(f.readline())
s = 0
l = float('inf')
min_s = [float('inf')] * 43
min_l = [10 * 10] * 43
max_s = 0
for i in range(N):
    x = int(f.readline())
    s += x
    ost = s % 43
    if min_s[ost] != float('inf'):
        if s - min_s[ost] > max_s or s - min_s[ost] == max_s and i - min_l[ost] < l:
            l = i - min_l[ost]
    if s < min_l[ost]:
        min_s[ost] = s
        min_l[ost] = i
print(l)
# Послед. из натур чисел N. Рассматриваются все непрерывные подпоследовательности, такие что
# сумма элементов каждой из них кратна k = 43. Найдите среди них с макс. суммой определите её длину.
# Если таких подпослед. несколько укажите длину наибольшей из них.
