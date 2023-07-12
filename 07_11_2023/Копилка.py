def knapsack(E, F, N, coins):
    dp = [[0] * (F + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        Pi, Wi = coins[i - 1]
        for j in range(F + 1):
            dp[i][j] = dp[i - 1][j]
            if Wi <= j:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - Wi] + Pi)

    if dp[N][F] == 0:
        return "This is impossible."
    else:
        return dp[N][F], dp[N][F]

E, F = map(int, input().split())
N = int(input())
coins = []
for _ in range(N):
    Pi, Wi = map(int, input().split())
    coins.append((Pi, Wi))

result = knapsack(E, F, N, coins)
if result == "This is impossible.":
    print(result)
else:
    min_sum, max_sum = result
    print(min_sum, max_sum)
