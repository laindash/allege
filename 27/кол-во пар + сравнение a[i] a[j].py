f = open('file.txt')
N = int(f.readline())
a = [0] * 34
count = 0
for i in range(N):
    x = int(f.readline())
    if x >= 34:
        continue
    for y in range(34):
        if x + y <= 34 and y > x:
            count += a[y]
    a[x] += 1
print(count)
# необходимо определить кол-во пар, сумма которых не более 34 и
# первый элемент больше второго (a[i] >  a[j] , i < j)
