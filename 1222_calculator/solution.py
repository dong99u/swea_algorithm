import sys
sys.stdin = open('input.txt')

t = 10

# 연산자 우선순위
level = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

def to_postfix(input_lst:list):
    result = [] # 후위 표기식으로 바뀐 결과
    stack = [] # 후위 표기식으로 바꾸기 위한 연산자 stack 정의

    for curr in input_lst:
        if curr.isdigit(): # 피연산자라면
            result.append(curr)
        else: # 연산자라면
            # stack의 top이 넣으려는 현재 연산자의 우선순위보다 같거나 높다면
            # 낮은 것이 나올 때까지 pop 후 result에 추가
            # 스택이 비어있다면 자동으로 stack에 추가
            if curr == '(': # 여는 괄호라면 그냥 추가
                stack.append(curr)
            elif curr == ')': # 닫는 괄호라면 여는 괄호가 나올 때까지 pop 후 result에 추가
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop() # 여는 괄호는 제거
            else: # 그냥 연산자라면
                while stack and level[stack[-1]] >= level[curr]:
                    result.append(stack.pop())
                stack.append(curr)

    # 스택에 남은 연산자 추가
    while stack:
        result.append(stack.pop())

    return result

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b

def get_result(lst: list):
    stack = []

    for curr in lst:
        if curr.isdigit(): # 피연산자라면 스택에 넣기
            stack.append(int(curr))
        else: # 연산자라면 stack의 top[-1], top[-2]를 pop해서 연산 후 다시 stack 에 넣기
            b = stack.pop()
            a = stack.pop()

            result = calculate(a, b, curr)

            stack.append(result)

    return stack.pop()


for tc in range(1, t + 1):
    n = int(input())

    input_lst = list(input())

    answer = get_result(to_postfix(input_lst))

    print(f'#{tc} {answer}')