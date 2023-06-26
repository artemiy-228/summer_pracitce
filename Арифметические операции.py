l = list(map(int, input().split()))
o = ["+", "-", "*", "//"]
count = 0

def oper(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    if a % b != 0 and a * b < 0:
        return a // b + 1
    return a // b


for i in o:
    for j in o:
        for k in o:
            a = oper(l[0], l[1], i)
            b = oper(a, l[2], j)
            if oper(b, l[3], k) == 0:
                count += 1

print(count)
