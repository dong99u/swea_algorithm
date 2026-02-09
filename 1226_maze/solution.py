import sys
sys.stdin = open('input.txt')
from collections import deque

N = 16
t = 10

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def find_points():
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1

    for x in range(N):
        for y in range(N):
            if grid[x][y] == 2:
                start_x, start_y = x, y
            if grid[x][y] == 3:
                end_x, end_y = x, y

    return (start_x, start_y), (end_x, end_y)

for _ in range(1, t + 1):
    test_case = int(input())

    grid = [
        list(map(int, list(input())))
        for _ in range(N)
    ]

    visited = [
        [False] * N
        for _ in range(N)
    ]

    (start_x, start_y), (end_x, end_y) = find_points()

    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    is_valid = False
    while q:
        curr_x, curr_y = q.popleft()

        if curr_x == end_x and curr_y == end_y:
            is_valid = True
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if not in_range(nx, ny):
                continue
            if grid[nx][ny] == 1:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))


    print(f'#{test_case} {1 if is_valid else 0}')
