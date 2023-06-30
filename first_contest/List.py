n = int(input())

l = [input() for i in range(n)]
l = sorted(l, key=lambda x: (len(x), x))

for i in l:
    print(i)

