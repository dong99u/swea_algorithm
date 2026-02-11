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

    # 집들의 좌표를 넣어놓기
    points = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                points.append((x, y))

    answer = 0
    for x in range(n):
        for y in range(n):
            points.sort(key=lambda p: get_manhattan_dist(x, y, p[0], p[1]), reverse=True)
            for i in range(len(points)):
                bound_x, bound_y = points[i]
                k = get_manhattan_dist(bound_x, bound_y, x, y)

                cnt = 0
                for j in range(len(points)):
                    x2, y2 = points[j]

                    if get_manhattan_dist(x, y, x2, y2) <= k:
                       cnt += 1

                if is_profit(k + 1, cnt):
                    answer = max(answer, cnt)
                    break


    print(f'#{test_case} {answer}')