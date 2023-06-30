a, b = map(int, input().split())

l = [tuple(input().split()) for i in range(a)]

l = sorted(l, key=lambda x: int(x[-1]))
answer = sorted([l[j][0] for j in range(b)])

for i in answer:
    print(i)