for n in range(200000001, 500000000):
    s = []
    p = []
    for d in range(2, 200):
        if n % d == 0:
            s.append(d)
            p.append(n)
            if len(s) == 5:
                break
    if len(s) == 5:
        mn = s[0] * s[1] * s[2] * s[3] * s[4]
        if 0 < mn < p[0]:
            print(mn)
