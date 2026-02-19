import sys
sys.stdin = open('input.txt')

INF = float('inf')

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    graph = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] == 0:
                graph[i][j] = INF

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    answer = -1

    for i in range(n):
        for j in range(n):
            if graph[i][j] != INF and answer < graph[i][j]:
                answer = graph[i][j]

    print(f'#{test_case} {answer}')