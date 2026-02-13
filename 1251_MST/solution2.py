import sys, math
sys.stdin = open('input.txt')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] == rank[y]:
        parent[y] = x
        rank[x] += 1
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y

def get_dist(i, j):
    x1, y1 = coords[i]
    x2, y2 = coords[j]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def get_weight():
    return

t = int(input())

for test_case in range(1, t + 1):

    n = int(input())

    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    coords = [(x, y) for x, y in zip(x_list, y_list)]

    parent = [i for i in range(len(coords))]
    rank = [0] * len(coords)

    E = float(input())

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            edges.append((i, j, get_dist(i, j)))

    edges.sort(key=lambda x: x[2])

    answer = 0
    for u, v, w in edges:
        if find(u) != find(v):
            answer += E * w
            union(u, v)

    print(f'#{test_case} {int(round(answer, 0))}')