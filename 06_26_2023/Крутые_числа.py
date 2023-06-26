num = int(input())
arr = [i**6 for i in range(1, 1001)]

for i in arr:
    if i > num:
        print(i)
        break