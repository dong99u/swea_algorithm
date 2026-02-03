import sys
sys.stdin = open('input.txt')

t = int(input())

def get_winner():
    global win_cnt, lose_cnt

    sum_point1 = 0 # 규영
    sum_point2 = 0 # 인영

    for i in range(9):
        if arr[i] > selected[i]:
            sum_point1 += arr[i] + selected[i]
        else:
            sum_point2 += arr[i] + selected[i]

    if sum_point1 > sum_point2:
        win_cnt += 1
    elif sum_point1 < sum_point2:
        lose_cnt += 1


def dfs(depth):
    if depth == 9:
        get_winner()
        return

    for i in range(9):
        if not visited[i]:
            selected.append(remain[i])
            visited[i] = True

            dfs(depth + 1)

            selected.pop()
            visited[i] = False

for tc in range(1, t + 1):
    arr = list(map(int, input().split())) # 규영이 카드

    remain = [card for card in range(1, 18 + 1) if card not in arr] # 인영이 카드

    visited = [False] * 9
    selected = []
    win_cnt = 0
    lose_cnt = 0

    dfs(0)

    print(f'#{tc} {win_cnt} {lose_cnt}')