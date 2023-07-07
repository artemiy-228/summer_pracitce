r, k = map(int, input().split())
sum = r * 100 + k
k = 0

for i in [500, 200, 100, 50, 10, 5, 1]:
    k += sum // i
    sum %= i
    if sum == 0:
        break

print(k)

