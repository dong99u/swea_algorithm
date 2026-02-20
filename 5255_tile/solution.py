import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):

    n = int(input())

    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1
    dp[2] = 3


    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2 + dp[i - 3]

    print(f'#{test_case} {dp[n]}')

