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
        return 'b1'                             # 21 если у вани есть стратегия в (12) all, ищем b1
    if any(f(m) == 'b1' for m in moves(s)):  # 20 в (12) меняем any на all, ищем p2 по условию
        return 'p2'
    if all(f(m) == 'p1' or f(m) == 'p2' for m in moves(s)):  # 21 в (12) all, ищем b1/2 если у вани есть + нет стратегии
        return 'b1/2'
for s in range(1, 72):    # значение по условию
    r = f((6, s))   # пишем первоначальное число камней и s, берём в двойные скобки
    if r is not None:
        print(s, r)
