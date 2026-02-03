import sys
sys.stdin = open('input.txt')

t = int(input())

def check(mx, my, x, y):
    return abs(x - mx) + abs(y - my) <= n // 2

for tc in range(1, t + 1):
    n = int(input())

    grid = [
        list(map(int, input()))
        for _ in range(n)
    ]

    answer = 0
    for i in range(n):
        for j in range(n):
            if check(n // 2, n // 2, i, j):
                answer += grid[i][j]

    print(f'#{tc} {answer}')
