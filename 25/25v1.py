a = 210235
b = 210300
for x in range(a, b + 1):
    D = set()
    for d in range(2, int(x ** 0.5) + 1):   # если в условии не считая 1 и самого числа, то range от 2, иначе от 1
        if x % d == 0:
            D.add(d)
            D.add(x // d)
    if len(D) == 4:
        print(*(sorted(D)))