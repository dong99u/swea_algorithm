import sys
sys.stdin = open('input.txt')

t = int(input())

def update_laser_cnt():
    for i in range(len(laser_cnt_stack)):
        laser_cnt_stack[i] += 1

for tc in range(1, t + 1):

    lst = input()

    stack = [] # 괄호 계산용 스택
    laser_cnt_stack = [] # 레이저 개수 계산용 스택

    answer = 0

    prev = None # 직전의 상태를 저장
    for elem in lst:
        if elem == '(':
            stack.append(elem)
            # 만약 현재 값이 ( 이고 직전 값이 (면 쇠막대기이므로 lazer cnt stack에 0을 추가
            if prev == '(':
                laser_cnt_stack.append(0)

        else:
            # 현재 값이 ) 이고 직전 값이 ( 라면 레이저 이므로 lazer cnt stack 를 모두 1씩 증가
            if prev == '(':
                stack.pop()
                update_laser_cnt()
            else:
                stack.pop()
                answer += laser_cnt_stack.pop() + 1
        prev = elem

    print(f'#{tc} {answer}')