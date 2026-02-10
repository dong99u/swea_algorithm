import heapq
import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    h = []

    answer = []

    for _ in range(n):
        inst = list(map(int, input().split()))

        if inst[0] == 1:
            heapq.heappush(h, -inst[1])
        else:
            if len(h) == 0:
                answer.append(-1)
            else:
                answer.append(-heapq.heappop(h))

    print(f'#{test_case}', *answer)