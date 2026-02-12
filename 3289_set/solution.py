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

    result = []
    parent = [i for i in range(n + 1)]
    for _ in range(m):
        inst, a, b = map(int, input().split())

        if inst == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                result.append(1)
            else:
                result.append(0)

    answer = ''.join(map(str, result))

    print(f'#{test_case} {answer}')