from itertools import permutations

n = int(input())

numbers = list(map(str, input().split()))

max1 = -1
answer = numbers
sublists = list(permutations(numbers, n))

for i in sublists:
    if int("".join(i)) > max1:
        max1 = int("".join(i))
        answer = i

print(" ".join(answer))