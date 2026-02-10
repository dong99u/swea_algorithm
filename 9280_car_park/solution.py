import sys
sys.stdin = open('input.txt')
import heapq
from collections import defaultdict, deque

'''
n = 주차 공간의 개수 (1 ~ n)
m = 들어오는 차량의 수
r = i번째 주차 공간의 단위 무게당 요금 리스트
w = i번 차량의 무게 (차량번호i와 도착 순서는 상관x)
'''

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    # 0-indexed
    r = []
    w = []
    for _ in range(n):
        r.append(int(input()))

    for _ in range(m):
        w.append(int(input()))

    # 비어있는 주차장 리스트
    h = [] # (i 번째 주차 번호, 단위 무게당 금액)
    for i, ri in enumerate(r):
        heapq.heappush(h, (i, ri))

    answer = 0

    first_entry = deque()

    for _ in range(2 * m):
        car_num = int(input())
        first_entry.append(car_num)

    wait = deque()
    wait.append(first_entry.popleft())

    # 사용중인 차량번호: 주차번호
    used = defaultdict(int)
    while wait:
        car_num = wait.popleft()
        # 들어오는 차량
        if car_num > 0:
            if not h:
                wait.appendleft(car_num - 1)
                continue
            i, ri = heapq.heappop(h)
            cost = w[car_num - 1] * ri
            answer += cost
            used[car_num - 1] = i
        # 나가는 차량
        elif car_num < 0:
            i = used[car_num - 1]
            del used[car_num - 1]
            heapq.heappush(h, (i, r[i]))

        if first_entry:
            wait.append(first_entry.popleft())

    print(f'#{test_case} {answer}')