import sys
sys.stdin = open('input.txt')

# 순회를 돌면서 이겼는지 판단
def win(arr):
    n = len(arr)
    same_cnt = 1
    increment_cnt = 1
    for i in range(1, n):
        if arr[i - 1] == arr[i]:
            same_cnt += 1
        else:
            if arr[i - 1] + 1 == arr[i]:
                increment_cnt += 1
            else:
                increment_cnt = 1
                same_cnt = 1

        if same_cnt >= 3 or increment_cnt >= 3:
            return True

    return False

t = int(input())

for test_case in range(1, t + 1):

    arr = list(map(int, input().split()))

    p1 = []
    p2 = []

    answer = 0
    # 카드 분배
    # 카드를 나눠줄 때마다 정렬한 다음 순회를 돌아서 이겼는지 판단
    for i, num in enumerate(arr):
        if i % 2 == 0:
            p1.append(num)
            p1.sort()
            if win(p1):
                answer = 1
                break
        else:
            p2.append(num)
            p2.sort()
            if win(p2):
                answer = 2
                break

    print(f'#{test_case} {answer}')
