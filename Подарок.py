import itertools
from math import prod

n, m = map(int, input().split())
lst = list(map(int, input().split()))

sum = 0

sublists = list(itertools.combinations(lst, m))

for i in sublists:
    sum += prod(i)

print(sum)
