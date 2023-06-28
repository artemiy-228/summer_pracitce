import math

primes = []
number = int(input())

while number % 2 == 0:
    number //= 2
    primes.append(2)

sqrt_number = math.isqrt(number)

for i in range(3, sqrt_number + 1, 2):
    while number % i == 0:
        number /= i
        primes.append(i)

if number > 1:
    primes.append(str(int(number)))

print("*".join(map(str, primes)))