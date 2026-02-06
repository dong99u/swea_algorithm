import sys
sys.stdin = open('input.txt')

def duplicated(r1, c1, r2, c2):
    return r1 == r2 and not (c1 + m <= c2 or c2 + m <= c1)

def dfs(honeys, idx, sum_val, profit):
    if idx == len(honeys):
        return profit

    pick = 0
    if sum_val + honeys[idx] <= c:
        pick = dfs(honeys, idx + 1, sum_val + honeys[idx], profit + honeys[idx] ** 2)

    skip = dfs(honeys, idx + 1, sum_val, profit)

    return max(pick, skip)

t = int(input())

for test_case in range(1, t + 1):
    n, m, c = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 1) 모든 가능한 위치별 최대 수익을 미리 계산
    profits = []  # (행, 열, 최대수익)
    for i in range(n):
        for j in range(n - m + 1):
            honeys = grid[i][j:j + m]
            if sum(honeys) <= c:
                p = sum(x ** 2 for x in honeys)
            else:
                p = dfs(honeys, 0, 0, 0)
            profits.append((i, j, p))

    # 2) 일꾼A와 일꾼B가 채취한 것들 중 겹치지 않는 두 위치 조합 중 최대값 찾기
    answer = 0
    for a in range(len(profits)):
        for b in range(a + 1, len(profits)):
            r1, c1, p1 = profits[a]
            r2, c2, p2 = profits[b]

            # 같은 행이면 구간이 겹치는지 체크
            if duplicated(r1, c1, r2, c2):
                continue

            answer = max(answer, p1 + p2)

    print(f'#{test_case} {answer}')