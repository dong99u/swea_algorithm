import sys
from collections import defaultdict
sys.stdin = open('input.txt')

t = int(input())

# X 상 하 좌 우
dxs = [0, -1, 1, 0, 0]
dys = [0, 0, 0, -1, 1]

next_dir = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

def is_edge(x, y):
    return x == 0 or x == n - 1 or y == 0 or y == n - 1

def move(dd: dict):
    # 미생물이 움직인 이후의 상태를 저장
    next_dd = defaultdict(list)

    # dd의 각 위치를 순회
    for (x, y), microbes in dd.items():
        # 해당 위치의 모든 미생물 그룹을 순회
        for cnt, dir_num in microbes:
            nx, ny = x + dxs[dir_num], y + dys[dir_num]

            # 미생물의 다음 위치가 약품 처리된 곳일 경우
            if is_edge(nx, ny):
                cnt //= 2  # 미생물 절반 죽음
                dir_num = next_dir[dir_num]  # 방향 반전

            # 미생물 수가 0이 아닌 경우만 추가
            if cnt > 0:
                next_dd[(nx, ny)].append((cnt, dir_num))

    return next_dd

def merge_microbes(dd: dict):
    """같은 위치의 미생물들을 합침"""
    merged_dd = defaultdict(list)

    for (x, y), microbes in dd.items():
        if len(microbes) > 1:
            # 가장 많은 미생물 수를 가진 그룹의 방향을 찾음
            max_cnt, max_dir = max(microbes, key=lambda m: m[0])

            # 모든 미생물 수를 합산
            total_cnt = sum(cnt for cnt, _ in microbes)

            # 합쳐진 미생물 저장
            merged_dd[(x, y)].append((total_cnt, max_dir))
        else:
            # 미생물이 1개면 그대로 저장
            merged_dd[(x, y)] = microbes

    return merged_dd

for tc in range(1, t + 1):
    n, m, k = map(int, input().split())

    # 미생물의 상태를 저장
    dd = defaultdict(list)

    for _ in range(k):
        x, y, cnt, dir_num = map(int, input().split())
        dd[(x, y)].append((cnt, dir_num))

    # m 시간 동안 시뮬레이션
    for _ in range(m):
        dd = move(dd)
        dd = merge_microbes(dd)

    # 최종 미생물 수 계산
    answer = 0
    for microbes in dd.values():
        for cnt, _ in microbes:
            answer += cnt

    print(f'#{tc} {answer}')