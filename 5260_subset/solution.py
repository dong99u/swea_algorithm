import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    dp = [
        [0] * (k + 1)
        for _ in range(n + 1)
    ]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i <= j:
                dp[i][j] = dp[i-1][j-i] + dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    print(f'#{test_case} {dp[n][k]}')