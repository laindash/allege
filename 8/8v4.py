# 5 буквенные слова, буквы встречаются 1 раз(permutations), не начинаются с Й, не содержат сочетание ИА
import itertools
a = list(itertools.permutations('КАЛИЙ', r=5))      # в permutations вместо repeat, r
count = 0
for x in a:
    x = ''.join(x)
    if x[0] != 'Й' and 'ИА' not in x:
        count += 1
print(count)
