f = open('file.txt')
N = int(f.readline())
s = [0]
for i in range(N):
    p = list(map(int, f.readline().split()))
    cmb = [a + b for a in s for b in p]
    s = {x % 3: x for x in sorted(cmb, reverse=True)}.values()  # max без reverse=True
print(min(x for x in s if x % 3 != 0))  # max
