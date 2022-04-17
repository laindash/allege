# 7 буквенные слова, в каждом слове комбинация КОТ, каждая буква встречается любое кол-во раз или не встречается
import itertools
a = list(itertools.product('ЕИЙКНОТ', repeat=7))
count = 0
for x in a:
    x = ''.join(x)
    if 'КОТ' in x:
        count += 1
print(count)