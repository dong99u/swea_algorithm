import sys
sys.stdin = open('input.txt')

from itertools import combinations

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    parent[y] = x

def get_dist(a, b):
    return (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    e = float(input())

    coords = []
    for idx, (x, y) in enumerate(zip(x_lst, y_lst)):
        coords.append((idx, x, y))

    edges = []
    for a, b in combinations(coords, 2):
        edges.append((get_dist(a, b), a[0], b[0]))

    edges.sort()

    parent = [i for i in range(n)]

    answer = 0.0
    for w, u, v in edges:
        if find(u) == find(v):
            continue

        answer += e * w
        union(u, v)

    print(f'#{test_case} {int(round(answer, 0))}')