a, b = map(int, input().split())
answer = list(map(int ,input().split()))
s = sum(answer) + 2 * abs(sum(sorted(answer)[:b]))
print(s)
