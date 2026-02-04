import sys
sys.stdin = open('input.txt')

N, S = 1, 2

t = 10
for tc in range(1, t + 1):
    n = int(input()) # 항상 100

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    answer = 0

    for row in zip(*grid):
        stack = []
        for mag in row: # 각 열의 자성 확인
            if mag == 0:
                continue
            if mag == N: # N극이라면 append
                stack.append(N)
            elif mag == S:
                # S극일 때 stack이 비어있다면 append
                # stack.top이 N극이라면 하나의 교착상태라고 판단
                if not stack:
                    stack.append(S)
                elif stack[-1] == N:
                    # 이전의 N극을 모두 합쳐서 하나의 교착 상태로 판단
                    # 만약 이 while 문을 사용하지 않는다면
                    # N, N, S, S 일 때 두 개의 교착 상태로 판단하게 됨.
                    while stack and stack[-1] != S:
                        stack.pop()
                    # stack.pop()
                    answer += 1

    print(f'#{tc} {answer}')

