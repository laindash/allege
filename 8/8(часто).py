# из ПАРУС составляются слова и записываются в алфавитном порядке, под каким номером начинается на У и нет АА рядом
from itertools import product
c = 0
for x in product('АПРСУ', repeat=5)):  # ставим буквы по алфавиту
    c += 1
    x = ''.join(x)
    if x[0] == 'У' and 'АА' not in x:
        print(c)
