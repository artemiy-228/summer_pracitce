T = int(input())
N = int(input())
components = [(0, 0, 0)]

for _ in range(N):
    cost, rating, comp_type = map(int, input().split())
    components.append((cost, rating, comp_type))

B = int(input())

dp = [[0] * (B+1) for _ in range(T+1)]
selected = [[0] * (B+1) for _ in range(T+1)]

for i in range(1, N+1):
    cost, rating, comp_type = components[i]
    for j in range(B, cost-1, -1):
        for k in range(1, T+1):
            if k == comp_type and dp[k-1][j-cost] + rating > dp[k][j]:
                dp[k][j] = dp[k-1][j-cost] + rating
                selected[k][j] = i

max_rating = dp[T][B]
if max_rating == 0:
    print(-1)
else:
    chosen_components = []
    j = B
    for i in range(T, 0, -1):
        index = selected[i][j]
        chosen_components.append(index)
        j -= components[index][0]

    print(max_rating)
    print(*chosen_components)
