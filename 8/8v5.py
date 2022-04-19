# слова составляются путём перестановки(permutations) букв в слове, сколько слов может получиться?
import itertools
a = list(set(itertools.permutations('БИТКОИН', r=7)))
print(len(a))
