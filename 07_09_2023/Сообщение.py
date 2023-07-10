s = input()
n = len(s)
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * int(int(s[i - 2]) != 0 and 0 < int(s[i - 2:i]) <= 33)

print(dp[-1])
