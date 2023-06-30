def div_count(x):
    c = 0
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x /= i
            c += 1
    if x != 1:
        c += 1
    return c


n = int(input())
max = -1
answ = 0

for i in range(1, n + 1):
    t = div_count(i)
    if t >= max:
        max = t
        answ = i

print(answ)

