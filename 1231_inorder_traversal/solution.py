import sys
sys.stdin = open('input.txt')

t = 10

def dfs(v):
    # basis
    if v >= n:
        return

    left = 2 * v + 1
    right = 2 * v + 2

    dfs(left)
    print(results[v], end='')
    dfs(right)

for tc in range(1, t + 1):

    n = int(input())

    results = [None] * n
    for _ in range(n):
        v, val = input().split()[:1 + 1]
        v = int(v) - 1

        results[v] = val

    print(f'#{tc}', end=' ')
    dfs(0)
    print()

