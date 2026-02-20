import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):

    n = int(input())

    a = list(map(int, input().split()))

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    answer = max(dp)

    print(f'#{test_case} {answer}')