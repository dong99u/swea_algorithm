import sys
sys.stdin = open('input.txt')

from collections import deque

t = int(input())

for tc in range(1, t + 1):
    n, m, k, lost_a, lost_b = map(int, input().split())
    a_lst = list(map(int, input()))
    
    d = deque()


