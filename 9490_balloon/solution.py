import sys
sys.stdin = open('input.txt')

t = int(input())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    # 하 우 상 좌
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    max_count = 0
    for x in range(n):
        for y in range(m):
            cnt = grid[x][y]
            power = cnt
            for dx, dy in zip(dxs, dys):
                for i in range(1, power + 1):
                    nx = x + dx * i
                    ny = y + dy * i

                    if not in_range(nx, ny):
                        continue

                    cnt += grid[nx][ny]

            if max_count < cnt:
                max_count = cnt

    print(f'#{tc} {max_count}')

