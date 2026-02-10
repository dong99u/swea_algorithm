nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
target_sum = 10
result = []

# 부분집합을 구성하는 모든 상황에 대한 처리는
# 2 ^ N
n = len(nums)
for i in range(1 << n):
    current_subset = [] # i번째 경우의 수에 만들어질 부분집합
    current_sum = 0
    for j in range(n):  # i번째 경우의 수에 j번 위치의 원소를 쓰는가?
        if i & (1 << j):
            current_subset.append(nums[j])
            current_sum += nums[j]
        if current_sum > target_sum: break
    if current_sum == target_sum:
        result.append(current_subset)
print(result)




