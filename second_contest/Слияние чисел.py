a = input()
b = input()

answer = ''

while len(a) > 0 or len(b) > 0:
    if a > b:
        answer += a[0]
        a = a[1:]
    else:
        answer += b[0]
        b = b[1:]

print(answer)
