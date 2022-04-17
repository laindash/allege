for a in range(0, 1000):    # значение от -1000, 0 или 1 в зависимости от условия
    k = 0
    for x in range(0, 1000):
        if x & 29 == 0 or (x & 17 != 0 or x & a != 0):      # замена A ⟶ B = ¬A ∨ B
            k += 1
    if k == 1000:
        print(a)
