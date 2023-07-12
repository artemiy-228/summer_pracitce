E, F = map(int, input().split())
N = int(input())
C = []
W = []
for _ in range(N):
    c, w = map(int, input().split())
    C.append(c)
    W.append(w)

len = F - E + 1
dp_max = [-1] * len
dp_min = [10000000000] * len
dp_min[0] = 0
dp_max[0] = 0

for i in range(N):
    for j in range(len - W[i]):
        dp_min[j + W[i]] = min(dp_min[j + W[i]], dp_min[j] + C[i])
        if dp_max[j] != -1:
            dp_max[j + W[i]] = max(dp_max[j + W[i]], dp_max[j] + C[i])

if dp_max[len - 1] == -1:
    print("This is impossible.")
else:
    print(dp_min[len - 1], dp_max[len - 1])
