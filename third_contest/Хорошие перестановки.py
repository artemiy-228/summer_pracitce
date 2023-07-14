n = int(input())
k = 1

while n >= k:
    if n == k:
        print(n, end=' ')
    else:
        print(n, k, end=' ', sep=' ')
    n -= 1
    k += 1