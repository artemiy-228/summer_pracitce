from itertools import combinations
from math import prod

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = list(combinations(arr, n))
arr.sort(key=lambda x: prod(x))
answer = 0

print(arr[-1])
