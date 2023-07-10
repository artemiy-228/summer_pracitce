dp = [0, 1]
n = int(input())

for i in range(2, n + 2):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[n + 1])