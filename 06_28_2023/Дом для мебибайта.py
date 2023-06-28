a, b = map(int, input().split())

c = a**2 + b**2

answer = int(c**0.5)

while answer * answer < c:
    answer += 1
print(answer - 1)
