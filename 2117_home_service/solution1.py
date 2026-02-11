import sys
sys.stdin = open('input.txt')

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def is_profit(k, cnt):
    '''

    :param k:
    :param cnt: 서비스 가능한 집의 개수
    :return:
    '''

    return (m * cnt) - ((k ** 2) + ((k - 1) ** 2)) >= 0

t = int(input())

for test_case in range(1, t + 1):

    n, m = map(int, input().split())

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    ggokji = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]

    answer = 0
    for mid_x in range(n):
        for mid_y in range(n):

            max_manhattan_dist = 0

            for x, y in ggokji:
                max_manhattan_dist = \
                    max(max_manhattan_dist, get_manhattan_dist(mid_x, mid_y, x, y))

            for k in range(1, max_manhattan_dist + 1 + 1):
                cnt = 0
                for x in range(mid_x - k + 1, mid_x + k):
                    for y in range(mid_y - k + 1, mid_y + k):
                        if not in_range(x, y):
                            continue
                        if grid[x][y] == 0:
                            continue

                        if grid[x][y] == 1 and get_manhattan_dist(mid_x, mid_y, x, y) < k:
                            cnt += 1

                if is_profit(k, cnt):
                    answer = max(answer, cnt)

    print(f'#{test_case} {answer}')