arr = [int(input()) for i in range(int(input()))]
arr.sort()

result = 0
c = 1
t = 0

print(arr)

for i in range(len(arr) - 1):
    t = arr[i]
    if arr[i + 1] == t:
        c += 1
    else:
        t = arr[i + 1]
        if c != 1:
            result += (c * (c - 1)) / 2
        c = 1
print(c)

