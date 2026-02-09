'''
N = 접수 창구 개수
M = 정비 창구 개수
K = 방문 고객 수
tk = k 번째 고객이 차량 정비소에 도착한 시간
ai = i 번째 접수 창구의 처리 시간
bi = i 번째 접수 창구의 처리 시간
'''

import sys
from collections import deque
sys.stdin = open('input.txt')


t = int(input())

for tc in range(1, t + 1):
    # A = 지갑을 잃어버린 고객이 이용했던 접수 창구 번호
    # B = 지갑을 잃어버린 고객이 이용했던 정비 창구 번호
    N, M, K, A, B = map(int, input().split())

    # 접수 창구의 처리 시간
    a = list(map(int, input().split()))
    # 정비 창구의 처리 시간
    b = list(map(int, input().split()))
    # 고객들의 도착 시간
    t = list(map(int, input().split()))


