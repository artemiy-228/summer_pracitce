import itertools

def is_prime(x):
    if x <= 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

number = [i for i in input()]
c = 0

for i in range(1, len(number) + 1):
    sublists = set(itertools.permutations(number, i))

    for j in sublists:
        if is_prime(int("".join(j))):
            c += 1
print(c)
