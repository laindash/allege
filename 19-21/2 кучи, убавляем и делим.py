import functools
import math
def moves(s):
    a, b = s
    return (a - 1, b), (a, b - 1), (math.ceil(a / 2), b), (a, math.ceil(b / 2))
# ПО УСЛОВИЮ. Округление в БОЛЬШУЮ сторону math.ceil(), в МЕНЬШУЮ math.floor()
@functools.lru_cache(None)
def f(s):
    if s[0] <= 1 or s[1] <= 1:  # пишем эту строчку всегда
        return
    if sum(s) <= 20:     # значение по условию
        return 'w'
    if any(f(m) == 'w' for m in moves(s)):
        return 'p1'
    if all(f(m) == 'p1' for m in moves(s)):   # №19 здесь меняем all на any ищем b1 по условию
        return 'b1'  # №21 если у Вани ЕСТЬ стратегия в (15 строка) all, ищем b1
    if any(f(m) == 'b1' for m in moves(s)):  # №20 в (15 строка) меняем any на all, ищем p2 по условию
        return 'p2'
    if all(f(m) == 'p1' or f(m) == 'p2' for m in moves(s)):  # №21 в (15) all, ищем b1/2 если у вани ЕСТЬ+НЕТ стратегии
        return 'b1/2'
for s in range(11, 100):    # значение по условию
    r = f((10, s))   # пишем первоначальное число камней и s, берём в ДВОЙНЫЕ СКОБКИ
    if r is not None:
        print(s, r)