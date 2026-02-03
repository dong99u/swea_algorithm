import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):


    n, k = map(int, input().split())

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if grid[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0

        if cnt == k:
            answer += 1

    for j in range(n):
        cnt = 0
        for i in range(n):
            if grid[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0

        if cnt == k:
            answer += 1

    print(f'#{tc} {answer}')

