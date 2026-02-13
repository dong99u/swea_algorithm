import sys
sys.stdin = open('input.txt')

import heapq

def kruskal():
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

        v, e = map(int, input().split())

        parent = [i for i in range(v + 1)]
        edges = []
        for _ in range(e):
            a, b, c = map(int, input().split())
            edges.append((a, b, c))

        edges.sort(key=lambda x: x[2])

        answer = 0
        for u, v, w in edges:
            if find(u) != find(v):
                answer += w
                union(u, v)

        print(f'#{test_case} {answer}')

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    node = 1 # prim 알고리즘에 의해 모든 노드들은 연결되어야하기 때문에 임의의 노드 아무거나 하나 잡아도 됨.

    hq = []
    visited = [False] * (n + 1)
    visited[node] = True
    for v, w in graph[node]:
        heapq.heappush(hq, (w, node, v))

    answer = 0
    # edge개만큼 돌아야함
    while hq:
        w, u, v = heapq.heappop(hq)
        if not visited[v]:
            answer += w
            visited[v] = True
            for next, weight in graph[v]:
                if not visited[next]:
                    heapq.heappush(hq, (weight, v, next))

    print(f'#{test_case} {answer}')


