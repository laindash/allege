# x = int(input())
#  L = 0
#  M = 0
# while x > 0 :
#   L = L+1
#   if (x % 2) != 0:
#       M = M + x % 8
#   x = x // 8
# print(L)
# print(M)
# Укажите наибольшее десятичное число, при вводе которого на экране сначала напечатается 3, а затем 6.
for k in range(0, 1000):
    x = k
    l = 0
    m = 0
    while x > 0:
        l = l + 1
        if x % 2 != 0:
            m = m + x % 8
        x = x // 8
    if l == 3 and m == 6:
        print(k)

