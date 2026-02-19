# import sys
# sys.stdin = open('input.txt')

INF = float('inf')

def get_cc(u):
    return sum([graph[u][v] for v in range(n)])


t = int(input())

for test_case in range(1, t + 1):
    n, *grid = list(map(int, input().split()))

    graph = [[0] * n for _ in range(n)]

    for idx, num in enumerate(grid):
        i = idx // n
        j = idx % n
        if i == j:
            graph[i][j] = 0
            continue
        elif i != j and num == 0:
            graph[i][j] = INF
            continue
        graph[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    results = []

    for u in range(n):
        results.append(get_cc(u))

    answer = min(results)

    print(f'#{test_case} {answer}')