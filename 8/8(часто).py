# из ПАРУС составляются слова и записываются в алфавитном порядке, под каким номером начинается на У и нет АА рядом
import itertools
a = list(itertools.product('АПРСУ', repeat=5))  # ставим буквы по алфавиту
count = 0
for x in a:
    count += 1
    x = ''.join(x)
    if x[0] == 'У' and 'АА' not in x:
        print(count)
        break
