isqrt = lambda c: (c**0.5 == int(c**0.5) or c**0.5 == int(c**0.5) + 1)

a, b = map(int, input().split())

c = (a**2 + b**2)
if isqrt(c):
    print(int(c**0.5) - 1)
else:
    print(int(c**0.5))