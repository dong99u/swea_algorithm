import sys, heapq
sys.stdin = open('input.txt')

t = int(input())

def kruskal(V, E, edges):
    parent = [i for i in range(V + 1)]
    rank = [0] * (V + 1)
    edges.sort(key=lambda edge: edge[2])

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if rank[x] == rank[y]:
            parent[y] = x
            rank[x] += 1
        elif rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x

    result = 0
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            result += w

    return result

def prim(V, E, edges):
    graph = [[] for _ in range(V + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    node = 1
    hq = []
    visited = [False] * (V + 1)
    visited[node] = True
    for v, w in graph[node]:
        heapq.heappush(hq, (w, v))
    result = 0
    while hq:
        w, v = heapq.heappop(hq)
        if not visited[v]:
            result += w
            visited[v] = True
            for next_v, next_w in graph[v]:
                if not visited[next_v]:
                    heapq.heappush(hq, (next_w, next_v))


    return result

for test_case in range(1, t + 1):

    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    answer = kruskal(V, E, edges)

    print(f'#{test_case} {answer}')