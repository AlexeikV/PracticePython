import random

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)

resultO = [i for i in set(a) if i in b]
result = [i for i in resultO if resultO.count(i) == 1]

