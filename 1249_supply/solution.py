import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for test_case in range(1, t + 1):
    n = int(input())

    grid = [
        list(map(int, list(input())))
        for _ in range(n)
    ]

    dist = [[-1] * n for _ in range(n)]

    start_x, start_y = 0, 0
    end_x, end_y = n - 1, n - 1

    q = deque([(start_x, start_y)])
    dist[start_x][start_y] = 0

    while q:
        curr_x, curr_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if not in_range(nx, ny):
                continue

            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[curr_x][curr_y] + grid[nx][ny]
                q.append((nx, ny))
                continue

            if dist[nx][ny] > dist[curr_x][curr_y] + grid[nx][ny]:
                dist[nx][ny] = dist[curr_x][curr_y] + grid[nx][ny]
                # 최단 경로로 갱신된 좌표만 큐에 넣어서 불필요한 경로 계산을 무시한다.
                q.append((nx, ny))

    print(f'#{test_case} {dist[end_x][end_y]}')

