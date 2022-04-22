f = open('file.txt')
N = int(f.readline())
a = [0, 0]
a1 = [0, 0]
count = 0
for i in range(N):
    x = int(f.readline())
    if x == 0:
        a[0] = a1[0]
        a[1] = a1[1]
        continue
    count += a[x % 2]
    a1[x % 2] += 1
print(count)
# Последоват. целых неотриц. чисел, нужно кол-во пар, у которых сумма чётна,
# между элементами есть хотя бы один 0
