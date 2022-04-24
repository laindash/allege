def f(i, n):
    a = '0123456789ABCDEF'
    b = a[i % n]
    while i >= n:
        i = i // n
        b += a[i % n]
    return b[::-1]


x1 = int(input('От '))
x2 = int(input('До(вкл) '))
for k in range(x1, x2 + 1):
    num = k
    global base
    s = []
    for r in range(2, 17):
        base = r
        bs = (f(int(num), base))
        s.append(bs)
    print(num)
    for l in range(len(s)):
        print('in', l + 2, ':', s[l], end='\n')
