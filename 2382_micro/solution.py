import sys
from collections import defaultdict
sys.stdin = open('input.txt')

t = int(input())

# X 상 하 좌 우
dxs = [0, -1, 1, 0, 0]
dys = [0, 0, 0, -1, 1]

def is_edge(x, y):
    return (x == 0 or x == n - 1) and (y == 0 or y == n - 1)

def move(dd: dict):
    # 미생물이 움직인 이후의 상태를 저장
    next_dd = defaultdict(list)
    for (x, y), (cnt, dir_num) in dd.items():
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        # 미생물이 약품처리된 (끝)에 있을 경우
        if not is_edge(nx, ny):

            continue

        next_dd[(nx, ny)].append((cnt, dir_num))



for tc in range(1, t + 1):
    n, m, k = map(int, input().split())

    # 미생물의 상태를 저장.
    dd = defaultdict(list)

    for _ in range(k):
        x, y, cnt, dir_num = map(int, input().split())
        dd[(x, y)].append((cnt, dir_num))

    for _ in range(m):
        move(dd)
