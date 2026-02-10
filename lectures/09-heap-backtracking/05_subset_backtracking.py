def subset(start, arr, acc):
    # 이 누적되어 온 값이... target_sum과 일치하면...
    if acc == target_sum:
        result.append(arr[:])
        return
    if acc > target_sum:
        return

    for i in range(start, len(nums)):
        num = nums[i]
        arr.append(num)
        subset(i + 1, arr, acc + num)
        arr.pop()


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []

subset(start=0, current_subset=[], acc=0)
