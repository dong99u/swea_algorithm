import sys
sys.stdin = open('input.txt')

import heapq

INF = float('inf')

t = int(input())

for test_case in range(1, t + 1):

    n, e = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    dist = [INF] * (n + 1)
    dist[0] = 0

    for _ in range(e):
        u, v, w = map(int, input().split())

        graph[u].append((v, w))


    hq = [(0, 0)]

    while hq:
        curr_dist, now = heapq.heappop(hq)

        for nxt, weight in graph[now]:
            if curr_dist + weight < dist[nxt]:
                dist[nxt] = curr_dist + weight
                heapq.heappush(hq, (curr_dist + weight, nxt))


    print(f'#{test_case} {dist[n]}')