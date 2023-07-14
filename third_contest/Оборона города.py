from collections import deque

def build_wall(plan):
    n = len(plan)
    m = len(plan[0])

    # Находим все важные здания
    buildings = []
    for i in range(n):
        for j in range(m):
            if plan[i][j] == '*':
                buildings.append((i, j))

    # Определяем границы, в которых нужно строить стену
    min_row = min(buildings, key=lambda x: x[0])[0]
    max_row = max(buildings, key=lambda x: x[0])[0]
    min_col = min(buildings, key=lambda x: x[1])[1]
    max_col = max(buildings, key=lambda x: x[1])[1]

    # Помечаем клетки для постройки стены
    wall_plan = [list(row) for row in plan]
    for i in range(n):
        for j in range(m):
            if wall_plan[i][j] != '*':
                if i == min_row or i == max_row or j == min_col or j == max_col:
                    wall_plan[i][j] = '#'

    return wall_plan

# Считываем входные данные
N, M = map(int, input().split())
plan = [input() for _ in range(N)]

# Строим стену
wall = build_wall(plan)

# Выводим результат
for row in wall:
    print(''.join(row))
