# 본인 인덱스, 본인 값, 왼쪽 자식 인덱스, 오른쪽 자식 인덱스
input_data = [
    [1, 'A', 2, 3],
    [2, 'B', 4, 0],
    [3, 'C', 0, 0],
    [4, 'D', 8, 0],
    [8, 'E', 0, 0],
]

n = 16
tree = [[None, None, None] for _ in range(n + 1)]

print(len(tree))
for idx in range(len(input_data)):
    my_idx = input_data[idx][0]
    value = input_data[idx][1]

    left = input_data[idx][2]
    right = input_data[idx][3]

    tree[my_idx] = [value, left, right]

