a, b = map(int, input().split())

primes = list(range(b + 1))
primes[0] = primes[1] = 0

i = 2

while i <= b:
    if primes[i] != 0:
        j = 2 * i
        while j <= b:
            primes[j] = 0
            j += i
    i += 1

answer = tuple(filter(lambda x: x >= a, primes))

if len(answer) == 0:
    print("Absent")
else:
    for i in answer:
        print(i)