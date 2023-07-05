K, M = map(int, input().split())
intervals = list(map(int, input().split()))

sum = 0
hours = 0

for hour in range(1, K + 1):
    interval = intervals[hour - 1]
    sum += interval
    if sum >= M:
        hours = hour
        break

print(hours)
