def is_divisible(nums, k):
    n = len(nums)
    dp = [[False] * (k+1) for _ in range(n+1)]
    dp[0][abs(nums[0]) % k] = True

    for i in range(1, n):
        for j in range(k):
            if dp[i-1][j]:
                dp[i][(j + nums[i]) % k] = True
                dp[i][(j - nums[i]) % k] = True

    return dp[n-1][0]

n, k = map(int, input().split())
nums = list(map(int, input().split()))

if is_divisible(nums, k):
    print("Divisible")
else:
    print("Not divisible")
