def d(n, m):    # всегда одинаково
    if n % m == 0:
        return 1
    else:
        return 0


for a in range(1, 1000):    # значение от -1000, 0 или 1 в зависимости от условия
    k = 0
    for x in range(1, 1001):    # в зависимости от условия нужно корректировать предел == k
        if d(x, a) or (not(d(x, 6)) or not(d(x, 4))):     # замена A ⟶ B = ¬A ∨ B
            k += 1
    if k == 1000:
        print(a)
