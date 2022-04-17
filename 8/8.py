# 3 буквенные слова, символ К один раз, остальные могут встречаться любое кол-во раз или не встречаться
import itertools
a = list(itertools.product('ШКОЛА', repeat=3))
count = 0
for x in a:
    if x.count('К') == 1:
        count += 1
print(count)
