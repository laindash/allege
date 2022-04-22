f = open('file.txt')
N = int(f.readline())
a = [float('inf')] * 30
s, k, = 0, 0
mx = -float('inf')
for i in range(N):
    x = int(f.readline())
    s += x
    if x > 0 and x % 2 == 0:
        k += 1
    mx = max(mx, s - a[k % 30])
    if k % 30 == 0:
        mx = max(mx, s)
    if s < a[k % 30]:
        a[k % 30] = s
print(mx)
# дана последовательность целых чисел. Необходимо найти макс.возм сумму подпоследоват., в которой
# кол-во положительных четных элементов кратно k = 30
