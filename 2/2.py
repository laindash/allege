print('x y z')     # + w если есть в условии
for x in range(2):
    for y in range(2):
        for z in range(2):      # for w in range(2) если есть w
            if ((not (x) and y and z) or (not (x) and not (y) and z) or (not (x) and not (y) and not(z))) == 1:
                # всю формулу взять в скобки и приравнять к 0 или 1 по условию таблицы
                # ^ = (and), v = (or), ¬ = (not) перед not всегда значение в скобках, ≡ = (==), → = (<=)
                print(x, y, z)



