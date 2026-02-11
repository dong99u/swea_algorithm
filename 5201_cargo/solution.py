import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):

    n, m = map(int, input().split())

    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort()
    t.sort()

    answer = 0
    for i in range(n - 1, -1, -1):
        if not t:
            break
        if w[i] <= t[-1]:
            answer += w[i]
            # 화물을 못 담는다고 해서 트럭을 pop하면 안됨.
            t.pop()

    print(f'#{test_case} {answer}')
