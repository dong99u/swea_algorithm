import sys
sys.stdin = open('input.txt')

# 상태 공간 트리 (예: nums=321, k=2, n=3)
# 가능한 swap: (0,1), (0,2), (1,2) → 매 depth마다 3개 가지
#
# memo에 저장하는 값: (상태문자열, depth)
#
#                          [3,2,1] depth=0
#                     memo: ('321',0) ✅ 신규
#                    /          |          \
#              (0,1)swap    (0,2)swap    (1,2)swap
#                /              |              \
#         [2,3,1] d=1      [1,2,3] d=1      [3,1,2] d=1
#       ('231',1)✅신규   ('123',1)✅신규   ('312',1)✅신규
#        /    |    \       /    |    \       /    |    \
#    (0,1) (0,2) (1,2) (0,1) (0,2) (1,2) (0,1) (0,2) (1,2)
#      |     |     |     |     |     |     |     |     |
# [3,2,1] [1,3,2] [2,1,3] [2,1,3] [3,2,1] [1,3,2] [1,3,2] [2,1,3] [3,2,1]
#  d=2     d=2    d=2     d=2     d=2     d=2     d=2     d=2     d=2
#
# ('321',2)✅  ('132',2)✅  ('213',2)✅
#  ans=321      ans=132      ans=213
#
#              ('213',2)❌  ('321',2)❌  ('132',2)❌
#               memo hit!   memo hit!   memo hit!
#
#                          ('132',2)❌  ('213',2)❌  ('321',2)❌
#                           memo hit!   memo hit!   memo hit!
#
# ─────────────────────────────────────────────────
# 결과: depth=2에서 실제 탐색은 3번만, 6번은 memo로 스킵!
# 최종 answer = 321
# ─────────────────────────────────────────────────

def dfs(curr_nums, depth):
    global answer

    state = (''.join(map(str, curr_nums)), depth)

    if state in memo:
        return
    memo.add(state)

    if depth == k:
        answer = max(answer, get_sum(curr_nums))
        return

    for i in range(n - 1):
        for j in range(i + 1, n):
            curr_nums[i], curr_nums[j] = curr_nums[j], curr_nums[i]
            dfs(curr_nums, depth + 1)
            curr_nums[i], curr_nums[j] = curr_nums[j], curr_nums[i]

def get_sum(arr):
    result = 0
    for i in range(n):
        result += arr[n - i - 1] * (10 ** i)

    return result


t = int(input())

for test_case in range(1, t + 1):

    nums, k = input().split()
    nums = list(map(int, list(nums)))
    k = int(k)

    n = len(nums)

    answer = 0

    memo = set()

    dfs(nums, 0)

    print(f'#{test_case} {answer}')