import sys
sys.stdin = open('input.txt')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    parent = [i for i in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    answer = len(set([find(i) for i in range(1, n + 1)]))

    print(f'#{test_case} {answer}')
