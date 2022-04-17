# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом
import re
s = open('file.txt').readline()
print(max(map(len, re.split(r'(?<=K)(?=L)|(?<=L)(?=K)', s))))
