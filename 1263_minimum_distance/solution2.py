from collections import deque

INF = float('inf')

def get_cc(u):
    return sum([graph[u][v] for v in range(n)])

def use_bfs_get_cc(v):
    q = deque([v])
    dist = [-1] * n
    dist[v] = 0
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    return sum(dist)


t = int(input())

for test_case in range(1, t + 1):
    n, *grid = list(map(int, input().split()))

    graph = [[] for _ in range(n)]

    for idx, num in enumerate(grid):
        i = idx // n
        j = idx % n
        if num == 1:
            graph[i].append(j)

    answer = INF

    for u in range(n):
        answer = min(answer, use_bfs_get_cc(u))

    print(f'#{test_case} {answer}')