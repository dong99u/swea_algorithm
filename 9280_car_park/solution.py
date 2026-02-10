import sys
sys.stdin = open('input.txt')
import heapq
from collections import deque

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    r = [int(input()) for _ in range(n)]
    w = [int(input()) for _ in range(m)]

    # 빈 주차 공간 힙 (번호가 작은 순)
    h = list(range(n))
    heapq.heapify(h)

    answer = 0
    used = {}       # 차량번호 -> 주차 공간 인덱스
    wait = deque()  # 대기 큐

    for _ in range(2 * m):
        car_num = int(input())

        if car_num > 0:  # 입차
            if h:
                spot = heapq.heappop(h)
                answer += w[car_num - 1] * r[spot]
                used[car_num] = spot
            else:
                wait.append(car_num)  # 자리 없으면 대기

        else:  # 출차
            out = -car_num
            spot = used.pop(out)
            heapq.heappush(h, spot)  # 자리 반납

            # 대기 차량이 있으면 즉시 배정
            if wait:
                next_car = wait.popleft()
                new_spot = heapq.heappop(h)
                answer += w[next_car - 1] * r[new_spot]
                used[next_car] = new_spot

    print(f'#{test_case} {answer}')