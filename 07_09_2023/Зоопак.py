n = int(input())
dp = [[0] * 4 for i in range(n+1)]

for i in range(1, n+1):
    t = int(input())
    dp[i][1] = dp[i-1][1] + t
    dp[i][2] = dp[i-1][2] + dp[i-1][1] * t
    dp[i][3] = dp[i-1][3] + dp[i-1][2] * t

print(dp[n][3])