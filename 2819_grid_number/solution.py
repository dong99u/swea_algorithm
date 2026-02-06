# import sys
# sys.stdin = open('input.txt')

def dfs(curr_x, curr_y, curr_list, depth):
    # basis
    if depth >= 7:
        answers.add(''.join(map(str, curr_list)))
        return

    for dx, dy in zip(dxs, dys):
        nx = curr_x + dx
        ny = curr_y + dy

        # 격자 바깥은 이동이 안됨.
        if not in_range(nx, ny):
            continue

        dfs(nx, ny, curr_list + [grid[nx][ny]], depth + 1)


# 격자 내부인지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

t = int(input())
n = 4 # 격자의 크기

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for test_case in range(1, t + 1):

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    answers = set()

    for curr_x in range(n):
        for curr_y in range(n):
            dfs(curr_x, curr_y, [grid[curr_x][curr_y]], 1)


    print(f'#{test_case} {len(answers)}')
