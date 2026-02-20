import sys
sys.stdin = open('input.txt')

def dfs(n, k):

    if k == 0:
        memo[n][k] = 1
        return 1
    if k == n: return 1

    if k == 1:
        memo[n][k] = n
        return n

    if memo[n][k] != 0:
        return memo[n][k]

    else:
        memo[n][k] = dfs(n - 1, k - 1) + dfs(n - 1, k)
        return memo[n][k]


t = int(input())

for test_case in range(1, t + 1):

    n, a, b = map(int, input().split())

    memo = [[0] * (n + 1) for _ in range(n + 1)]

    if a > n - a:
        a = n - a

    dfs(n, a)
    print(f'#{test_case} {memo[n][a]}')