with open('24v3.txt') as f:
    s = f.readline()
    k = 1
    kmax = 1
    c = 0
    for i in s:
        if 'kl' in i:
            k = 0
            c = k - 1
        else:
            k += 1
            kmax = max(kmax, k)
print(kmax)