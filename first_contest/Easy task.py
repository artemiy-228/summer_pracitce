n, x, y = map(int, input().split())

s = min(x, y)
l = 1
r = (n - 1) * min(x, y)
while r - l > 1:
    m = (r + l) // 2
    if n - 1 <= m // x + m // y:
        r = m
    else:
        l = m
print(r + min(x, y))