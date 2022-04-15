# если прибавляем или умножаем
import functools
def moves(s):
    a, b = s
    return (a + 1, b), (a, b + 1), (a * 3, b), (a, b * 3)    # значения по условию
@functools.lru_cache(None)
def f(s):
    if sum(s) >= 88:     # значение по условию
        return 'w'
    if any(f(m) == 'w' for m in moves(s)):
        return 'p1'
    if all(f(m) == 'p1' for m in moves(s)):   # 19 меняем на any, ищем b1 по условию
        return 'b1'                             # 21 если у вани есть стратегия в (11) all, ищем b1
    if any(f(m) == 'b1' for m in moves(s)):  # 20 в (11) меняем any на all, ищем p2 по условию
        return 'p2'
    if all(f(m) == 'p1' or f(m) == 'p2' for m in moves(s)):  # 21 в (11) all, ищем b1/2 если у вани есть + нет стратегии
        return 'b1/2'
for s in range(1, 72):    # значение по условию
    r = f((6, s))   # пишем первоначальное число камней и s, берём в двойные скобки
    if r is not None:
        print(s, r)
# если убавляем или делим
import functools
import math
def moves(s):
    a, b = s
    return (a - 1, b), (a, b - 1), (math.ceil(a / 2), b), (a, math.ceil(b / 2))
@functools.lru_cache(None)    # по условию округление в большую сторону math.ceil(), в меньшую math.floor()
def f(s):
    if s[0] <= 1 or s[1] <= 1: # всегда если кучи отнимаем или делим
        return
    if sum(s) <= 20:     # значение по условию
        return 'w'
    if any(f(m) == 'w' for m in moves(s)):
        return 'p1'
    if all(f(m) == 'p1' for m in moves(s)):   # 19 меняем на any, есть стратегия в (11) all, ищем b1
        return 'b1'  # 21 если у вани меняем any на all, ищем p2 по условию
    if any(f(m) == 'b1' for m in moves(s)):  # 20 в (11)  ищем b1 по условию
        return 'p2'
    if all(f(m) == 'p1' or f(m) == 'p2' for m in moves(s)):  # 21 в (11) all, ищем b1/2 если у вани есть + нет стратегии
        return 'b1/2'
for s in range(11, 100):    # значение по условию
    r = f((10, s))   # пишем первоначальное число камней и s, берём в двойные скобки
    if r is not None:
        print(s, r)