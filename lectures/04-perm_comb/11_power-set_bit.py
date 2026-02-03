arr = [1, 2, 3]
subsets = []

# for i in range(2 ** len(arr)):
for i in range(1 << len(arr)):
    subset = []

    # 내가 가진 N 개의 원소에 대해서
    # j 번째 요소가 이번 경우의 수에 포함되느냐
    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])
    subsets.append(subset)

print(subsets)
