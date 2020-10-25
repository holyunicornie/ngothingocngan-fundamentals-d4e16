sheeps = [5, 10, 40, 50, 3, 1, 4999, 14, 3]
#for sheep in range(len(sheeps)):
    #sheep += 50

max_number = sheeps[0]

for sheep in sheeps:
    if max_number < sheep:
        max_number = sheep    #import random thì phải random. trước lệnh
print(max_number)

#bài 3
from random import shuffle; sample
words = ["a", "b", "e", "f"]
a = sample(words, i)
print(a)
