# Назовём парой два идущих подряд элемента последовательности. Определите количество пар, в которых хотя бы один из двух
# элементов делится на 3 и хотя бы один из двух элементов меньше среднего арифметического всех чётных элементов
# последовательности. В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму
# элементов таких пар.
a = list(map(int, open('file.txt')))
count = 0   # количество найденных пар
s = []  # список со всеми суммами элементов пар
m = 0   # сумма четных или нечётных элементов
n = 0   # количество четных или нечетных элементов
for i in range(len(a)):
    if a[i] % 2 == 0:   # если в условии среднее арифметическое нечетных чисел, то заменяем на == 1
        m += a[i]
        n += 1
x = m / n
for i in range(len(a) - 1):
    if ((a[i] % 3 == 0) or (a[i + 1] % 3 == 0)) and ((a[i] < x) or (a[i + 1] < x)):
        count += 1
        s.append(a[i] + a[i + 1])
print(count, max(s))
