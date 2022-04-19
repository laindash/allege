# def F(n):
#     if n > 2:
#         return F(n-1)+ G(n-2)
#     else: return 1
# def G(n):
#     if n > 2:
#         return G(n-1) + F(n-2)
#     else: return 1
# Чему будет равно значение, вычисленное при выполнении вызова F(8)?
def f(n):
    if n > 2:
        return f(n - 1) + g(n - 2)
    else:
        return 1


def g(n):
    if n > 2:
        return g(n - 1) + f(n - 2)
    else:
        return 1


print(f(8))
