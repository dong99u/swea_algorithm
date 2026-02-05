import sys
sys.stdin = open('input.txt')

t = 10

def dfs(v):
    # 리프 노드(숫자)라면
    if tree[v]['type'] == 'number':
        return tree[v]['value']

    # 연산자 노드라면
    left = tree[v]['left']
    right = tree[v]['right']
    operator = tree[v]['operator']

    left_val = dfs(left)
    right_val = dfs(right)

    if operator == '+':
        return left_val + right_val
    elif operator == '-':
        return left_val - right_val
    elif operator == '*':
        return left_val * right_val
    elif operator == '/':
        return left_val / right_val


for tc in range(1, t + 1):
    n = int(input())

    tree = [None] * n

    for _ in range(n):
        input_lst = input().split()

        if len(input_lst) == 4:  # 연산자 노드
            v, operator, left, right = input_lst
            v = int(v) - 1
            left = int(left) - 1
            right = int(right) - 1

            tree[v] = {
                'type': 'operator',
                'operator': operator,
                'left': left,
                'right': right
            }

        else:  # 리프 노드 (숫자)
            v, num = input_lst
            v = int(v) - 1

            tree[v] = {
                'type': 'number',
                'value': int(num)
            }

    answer = int(dfs(0))

    print(f'#{tc} {answer}')