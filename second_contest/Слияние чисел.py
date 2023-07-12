x = input()
y = input()

i = 0
k = 0
answer = ""

if len(x) > len(y):
    x, y = y, x

while i < len(x):
    if x[i] > y[k]:
        answer += x[i]
        i += 1
    elif x[i] < y[k]:
        answer += y[k]
        k += 1
    else:
        if x[i] == y[k]:
            answer += x[i]
            n = i
            m = k
            while n < len(x) and m < len(y) and x[n] == y[m]:
                n += 1
                m += 1
            if n < len(x) and m < len(y):
                if x[n] > y[m]:
                    i += 1
                else:
                    k += 1
            else:
                break

answer += y[k:]

print(answer)
