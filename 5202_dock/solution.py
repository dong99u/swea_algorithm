import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    docks = []
    for _ in range(n):
        # 시작, 종료 시간
        s, e = map(int, input().split())
        docks.append((s, e))

    docks.sort(key=lambda x: (x[1], -x[0]))

    prev = docks[0]
    answer = 1
    for s, e in docks[1:]:
        if prev[1] <= s:
            answer += 1
            prev = (s, e)

    print(f'#{test_case} {answer}')


