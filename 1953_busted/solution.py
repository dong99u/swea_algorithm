# import sys
# sys.stdin = open('input.txt')
from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

t = int(input())

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 각 파이프마다 이동할 수 있는 방향
# dxs, dys의 인덱스
directions = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}

connected = {
    0: [1, 2, 5, 6], # 위로 움직였을 때 움직일 수 있는 파이프의 번호
    1: [1, 2, 4, 7], # 아래로 움직였을 때 이동할 수 있는 파이프의 번호
    2: [1, 3, 4, 5], # 왼쪽으로 움직였을 때 이동할 수 있는 파이프의 번호
    3: [1, 3, 6, 7] # 오른쪽으로 움직였을 때 이동할 수 있는 파이프의 번호
}

for test_case in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    visited = [
        [False] * m
        for _ in range(n)
    ]

    # 시작 지점과 함께 시작 시간을 같이 넣음.
    q = deque([(r, c, 0)])
    # bfs는 시작지점을 미리 방문 처리한다.
    visited[r][c] = True

    answer = 0
    while q:
        curr_x, curr_y, t = q.popleft()

        # 탈출 후 소요시간과 같은 게 나오면 멈춤.
        if t == l:
            break
        answer += 1

        for dir_num in directions[grid[curr_x][curr_y]]:
            dx, dy = dxs[dir_num], dys[dir_num]

            nx, ny = curr_x + dx, curr_y + dy

            if not in_range(nx, ny):
                continue

            if grid[nx][ny] not in connected[dir_num]:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny, t + 1))


    print(f'#{test_case} {answer}')




