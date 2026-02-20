import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):

    # n = 박스의 크기
    # m = 상품의 개수
    n, m = map(int, input().split())

    S = []
    P = []
    for _ in range(m):
        s, p = map(int, input().split())

        S.append(s)
        P.append(p)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j - S[i - 1]] + P[i - 1], dp[i - 1][j])

            else:
                dp[i][j] = dp[i - 1][j]

    answer = dp[m][n]

    print(f'#{test_case} {answer}')