from itertools import permutations

string = input()

arr = ["".join(i) for i in list(permutations(string))]
arr.sort(reverse=True)


print(arr)