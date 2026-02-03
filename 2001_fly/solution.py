import sys
sys.stdin = open('input.txt')

t = int(input())

def get_cnt(x, y):
    cnt = 0
    for i in range(m):
        for j in range(m):
            nx = x + i
            ny = y + j

            cnt += grid[nx][ny]

    return cnt

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    max_cnt = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = get_cnt(i, j)

            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')