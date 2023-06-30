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

answer = set()
c = 0

for i in range(1, len(number) + 1):
    sublists = list(itertools.permutations(number, i))

    for j in range(len(sublists)):
        sublists[j] = int("".join(sublists[j]))

    for i in sublists:
        answer.add(i)

for i in answer:
    if is_prime(i):
        c += 1
print(c)
