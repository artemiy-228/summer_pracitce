from math import sqrt

f, k = map(int, input().split())

y = sqrt(f)
x = sqrt(k)
x1 = k

print(x - y) if x1 * x1 > y * y else print(x - y + 1)