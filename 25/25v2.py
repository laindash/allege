c = 0
for i in range(600000, 10000000):
    md = 0
    for d in range(1, int(i ** 0.5) + 1):
        if i % d == 0:
            if d % 10 == 7 and d != 7:
                md = d
                break
    if md > 0:
        print(i, md)
        c += 1
        if c == 5:
            break
