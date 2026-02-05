# import sys
# sys.stdin = open('input.txt')

"""
중위 순회 LMR 문제
"""
t = int(input())

def dfs(curr_idx):
    global cnt

    # 현재 인덱스가 n 보다 크면 트리 범위를 초과
    if curr_idx >= n:
        return

    left = 2 * curr_idx + 1
    right = 2 * curr_idx + 2

    dfs(left)
    results[curr_idx] = cnt
    cnt += 1
    dfs(right)

for tc in range(1, t + 1):
    n = int(input())
    results = [None] * n

    cnt = 1
    dfs(0)

    answer1 = results[0]
    answer2 = results[n // 2 - 1]

    print(f'#{tc} {answer1} {answer2}')