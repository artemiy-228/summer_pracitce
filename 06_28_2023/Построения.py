n = int(input())

def div_count(x):
    if x <= 1:
        return 1
    c = 2
    d = 2
    while d * d < x:
        if x % d == 0:
            c += 2
        d += 1
    if d * d == x:
        c += 1
    return c

print(div_count(n))