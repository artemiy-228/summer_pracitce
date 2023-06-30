n = int(input())
answers=[]

def calculate(s, cords):
    for j in range(1, s):
        for k in range(1, s):
            max = -1
            for c in cords:
                if ((c[0] - j) ** 2 + (c[1] - k) ** 2) ** 0.5 >= max:
                    max = ((c[0] - j) ** 2 + (c[1] - k) ** 2) ** 0.5

            if s - j >= max and j >= max and s - k >= max and k >= max:
                return f"dog {j} {k}"
    return "robot"


for i in range(n):
    s, h = map(int, input().split())
    cords = []

    for j in range(h):
        cords.append(tuple(map(int, input().split())))

    answers.append(calculate(s, cords))

for i in answers:
    print(i)





