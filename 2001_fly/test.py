# import sys
# sys.stdin = open('sample_input.txt')
from collections import deque

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    degree = [-1] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    q = deque()

    for _ in range(n):
        e, *ss = map(int, input().split())

        if e == 0:
            continue

        for s in ss:
            graph[s].append(e)
            if degree[s] == -1:
                degree[s] = 0
            if degree[e] == -1:
                degree[e] = 0
            degree[e] += 1

    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)

    answer = 0  # 학기 수
    processed = 0  # 처리한 과목 수 (사이클 검증용)

    while q:
        size = len(q)  # 이번 학기에 수강할 과목 수
        for _ in range(size):
            nxt = q.popleft()
            processed += 1
            for now in graph[nxt]:
                degree[now] -= 1
                if degree[now] == 0:
                    q.append(now)
        answer += 1  # 한 학기 완료

    # 사이클 검증: 처리된 과목 수가 전체 과목 수와 같은지 확인
    total = sum(1 for i in range(1, n + 1) if degree[i] != -1)
    is_valid = (processed == total)

    print(f'#{test_case} {answer if is_valid else -1}')


