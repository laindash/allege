# Найдите все натуральные числа N, принадлежащие отрезку [400000000;600000000], которые можно представить в виде N=2m·3n
# где m— чётное число, n— нечётное число. В ответе запишите все найденные числа в порядке возрастания.
for m in range(2, 1000, 2):
    for n in range(1, 1001, 2):
        if 400000000 < 2 ** m * 3 ** n < 600000001:
            print(2 ** m * 3 ** n)
