import sys
sys.stdin = open('input.txt')

def dfs(curr_nums, depth):
    global answer
    if depth == k:
        answer = max(answer, get_sum(curr_nums))
        return

    for i in range(n - 1):
        for j in range(i + 1, n):
            curr_nums[i], curr_nums[j] = curr_nums[j], curr_nums[i]
            dfs(curr_nums, depth + 1)
            curr_nums[i], curr_nums[j] = curr_nums[j], curr_nums[i]

def get_sum(curr_nums: list):

    multi = 1
    result = 0
    for num in curr_nums[::-1]:
        result += num * multi
        multi *= 10

    return result

t = int(input())

for test_case in range(1, t + 1):

    nums, k = input().split()
    nums = list(map(int, list(nums)))
    k = int(k)

    n = len(nums)

    answer = 0

    dfs(nums, 0)

    print(f'#{test_case} {answer}')
