a = list(map(int, open('file.txt')))
I = set()
J = set()
for i in range(len(a) - 1):
    if a[i] % 7 == 0 and a[i] % 49 != 0:
        I.add(a[i])
    if a[i] % 7 != 0 and a[i] % 49 != 0:
        J.add(a[i])
print(*sorted(I))
print(*sorted(J))
# По каналу связи передавались данные в виде последовательности положительных целых чисел.
# Количество чисел заранее неизвестно, но не менее двух, признаком конца данных считается число 0. Контрольное значение
# равно такому максимально возможному произведению двух чисел из переданного набора, которое делится на 7, но не делится
# на 49. Если такое произведение получить нельзя, контрольное значение считается равным 1.
# Программа должна напечатать одно число — вычисленное контрольное значение, соответствующую условиям задачи.