# 5 значные числа в шестиричной системе, цифры в числе могут повторяться, две четные или нечетные не стоят рядом
import itertools
a = list(itertools.product('012345', repeat=5))
count = 0
f1 = list(itertools.product('024', repeat=2))
f2 = list(itertools.product('135', repeat=2))
f = f1 + f2
for x in a:
    x = ''.join(x)
    if all(''.join(s) not in x for s in f) and x[0] != '0':
        count += 1
print(count)
