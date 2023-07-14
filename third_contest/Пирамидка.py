def reverse(n):
    answ = arr[:n]
    return answ[::-1] + arr[n:]

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
res = []

while n != 1:
    if (n == arr[n - 1]):
        n -= 1
        continue

    for i in range(n):
        if arr[i] == n:
            if i > 0:
                arr = reverse(i + 1)
                res.append(i + 1)
                cnt += 1
            arr = reverse(n)
            res.append(n)
            cnt += 1
            break

print(cnt, *res, sep=' ')