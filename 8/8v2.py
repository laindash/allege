# 4 буквенные слова, не начинаются с Й, содержат хотя бы одну гласную
import itertools
a = list(itertools.product('ГАФНИЙ', repeat=4))
count = 0
for x in a:
    if x[0] != 'Й' and ('А' in x or 'И' in x):
        count += 1
print(count)
