def f(i, n):
    a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = a[i % n]
    while i >= n:
        i //= n
        b += a[i % n]
    return b[::-1]
for x in range(2, 35):
    num = input()
    base = 10
    t_base = x
    s = int(num, base)
    s = f(s, t_base)
    print(s, t_base)
