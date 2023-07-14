n = int(input())

digits = [int(input()) for i in range(n)]
digits.sort()
medium = digits[0]

for i in range(1, len(digits)):
    medium = (medium + digits[i]) / 2

print('%.6f' % medium)