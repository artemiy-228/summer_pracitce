n = int(input())
arr = tuple(filter(lambda x: x != (0, 0), list(zip(list(map(int, input().split())), list(map(int, input().split()))))))

c = 1

for i in range(1, len(arr)):
    if arr[i] == (1, 1):
        c += 1
    elif arr[i] == (1, 0) and arr[i - 1] != (1, 0) or arr[i] == (0, 1) and arr[i - 1] != (0, 1):
        c += 1

if len(arr) == 0:
    c = 0
print(c)


