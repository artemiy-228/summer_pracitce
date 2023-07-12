n = int(input())
arr = [list(map(int, list(input()))) for i in range(n)]
path = []
cost = [[0] * n for _ in range(n)]
cost[0][0] = arr[0][0]

for i in range(1, n):
    cost[0][i] = cost[0][i - 1] + arr[0][i]
    cost[i][0] = cost[i - 1][0] + arr[i][0]

for i in range(1, n):
    for j in range(1, n):
        cost[i][j] = min(cost[i - 1][j], cost[i][j - 1]) + arr[i][j]

start = (0, 0)
end = (n - 1, n - 1)

def restore_path():
    i, j = end
    path.append((i, j))

    while (i, j) != start:
        if i > 0 and j > 0:
            if cost[i - 1][j] < cost[i][j - 1]:
                i -= 1
            else:
                j -= 1
        elif i > 0:
            i -= 1
        else:
            j -= 1

        path.append((i, j))

restore_path()

for i in range(n):
    for j in range(n):
        if (i, j) in path:
            print("#", end="")
        else:
            print("-", end="")
    print()

