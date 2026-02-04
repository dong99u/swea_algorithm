from collections import deque
import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(1, T + 1):
    tc = int(input())

    # 시작 암호 코드 초기화
    q = deque(list(map(int, input().split())))

    is_valid = True
    while is_valid:
        for i in range(1, 5 + 1):
            popleft = q.popleft()
            after = popleft - i

            if after <= 0:
                is_valid = False
                q.append(0)
                break

            q.append(after)



    answer = list(q)
    print(f'#{tc}', *answer)