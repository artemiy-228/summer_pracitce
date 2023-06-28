def isqrt(num):
    if num**0.5 == int(num**0.5) or num**0.5 == int(num**0.5) + 1:
        return True
    return False

num = int(input())

arr = [i**3 for i in range(1, num)]

for i in arr:
    if isqrt(i) and i > num:
        print(i)
        break

