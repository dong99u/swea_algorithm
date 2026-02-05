'''
n = 접수 창구 개수
m = 정비 창구 개수
k = 방문 고객 수
tk = k 번째 고객이 차량 정비소에 도착한 시간
ai = i 번째 접수 창구의 처리 시간
bi = i 번째 접수 창구의 처리 시간
'''

import sys
from collections import deque
import heapq
sys.stdin = open('input.txt')


t = int(input())

for tc in range(1, t + 1):
    # lost_a_num = 지갑을 잃어버린 고객이 이용했던 접수 창구 번호
    # lost_b_num = 지갑을 잃어버린 고객이 이용했던 정비 창구 번호
    n, m, k, lost_a_num, lost_b_num = map(int, input().split())
    a_list = list(map(int, input().split())) # 접수 창구들의 처리시간
    b_list = list(map(int, input().split())) # 정비 창구들의 처리시간
    tk_list = list(map(int, input().split())) # 고객들의 차량 정비소 도착 시간 정보

    visited_customer_waiting_queue = deque() # [(고객 번호, 고객이 도착한 시간), ...]

    for cust_num, tk in enumerate(tk_list):
        visited_customer_waiting_queue.append((cust_num, tk))

    available_a_queue = [] # 이용 가능한 접수 창구
    available_b_queue = [] # 이용 가능한 정비 창구

    for ai in a_list:
        heapq.heappush(())

    temp_queue = [] # 접수 후 정비 하기 전에 대기하는 고객의 큐

    curr_time = 0
    while True:








