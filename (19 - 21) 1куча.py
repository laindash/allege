import functools
def moves(s):
    return s + 1, s + 4, s * 5    # значения по условию
@functools.lru_cache(None)
def f(s):
    if s >= 68:     # значение по условию
        return 'w'
    if any(f(m) == 'w' for m in moves(s)):
        return 'p1'
    if all(f(m) == 'p1' for m in moves(s)):   # 19 меняем на any, ищем b1 по условию
        return 'b1'
    if any(f(m) == 'b1' for m in moves(s)):  # 20 в (10) меняем any на all, ищем p2 по условию
        return 'p2'
    if all(f(m) == 'p1' or f(m) == 'p2' for m in moves(s)):  # 21 в (10) all, ищем b1/2 по условию
        return 'b1/2'
for s in range(1, 68):    # значение по условию
    r = f(s)
    if r is not None:
        print(s, r)
