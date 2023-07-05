n = int(input())

l = list(map(str, input().split()))
l.sort(key=lambda x: (x[0],x[1] -len(x)), reverse=True)

print(" ".join(l))
