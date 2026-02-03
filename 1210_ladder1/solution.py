import sys
sys.stdin = open('input.txt')

n = 100

def dfs(x, y):
    while True:
        if y > 0 and grid[x][y - 1] == 1:
            while y > 0 and grid[x][y - 1] == 1:
                y -= 1
        elif y < n - 1 and grid[x][y + 1] == 1:
            while y < n - 1 and grid[x][y + 1] == 1:
                y += 1
        x += 1

        if x == n - 1:
            break

    return True if grid[x][y] == 2 else False

for _ in range(10):
    tc = int(input())

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    start_y_lst = [y for y in range(n) if grid[0][y] == 1]

    answer = -1

    for start_y in start_y_lst:

        if dfs(0, start_y):
            answer = start_y
            break

    print(f'#{tc} {answer}')