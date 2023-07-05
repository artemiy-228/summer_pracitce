from sys import setrecursionlimit

setrecursionlimit(100000)

count = 0
matrix = [[False] * 100 for _ in range(100)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def check(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    if not check(y, x) or matrix[y][x] == True:
        return

    matrix[y][x] = True

    for i in range(4):
        dfs(y + dy[i], x + dx[i])


def count_pieces():
    global count
    for i in range(n):
        for j in range(m):
            if not matrix[i][j]:
                count += 1
                dfs(i, j)


n, m = map(int, input().split())

for i in range(n):
    row = input()
    for j in range(m):
        matrix[i][j] = row[j] == '.'

count_pieces()

print(count)
