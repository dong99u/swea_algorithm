# import sys
# sys.stdin = open('input.txt')
#
t = int(input())

operator = [
    lambda a, b: a + b,
    lambda a, b: a - b,
    lambda a, b: a * b,
    lambda a, b: int(a / b) # 파이썬의 // 연산자는 음의 무한대 방향으로 내림처리를 하기 때문에 나누고 정수값만 구한다.
]

def dfs(cal_result, depth):
    global max_num, min_num
    # basis
    if depth == n - 1:
        max_num = max(max_num, cal_result)
        min_num = min(min_num, cal_result)
        return

    for i in range(4):
        if visited[i] < operators[i]: # 해당되는 연산자를 모두 사용하지 않았으면
            visited[i] += 1
            dfs(operator[i](cal_result, nums[depth + 1]), depth + 1)
            visited[i] -= 1


for test_case in range(1, t + 1):
    # 숫자의 개수
    n = int(input())
    # 연산자들의 개수 +, -, *, /
    operators = list(map(int, input().split()))
    # 연산자들을 모두 몇개 사용했는지
    visited = [0] * 4
    # 숫자들
    nums = list(map(int, input().split()))

    max_num = -1e9
    min_num = 1e9

    dfs(nums[0], 0)

    answer = max_num - min_num

    print(f'#{test_case} {answer}')