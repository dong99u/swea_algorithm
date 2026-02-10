import sys
sys.stdin = open('input.txt')

def back_track(idx, sum_val):
    global answer

    # 모든 조합을 다 고려했을 때,
    if idx == n:
        # 하나라도 선택했고, 그 총합이 k개면 경우의 수 카운트.
        if sum_val != 0 and sum_val == k:
            answer += 1
        return

    if sum_val + arr[idx] <= k:
        back_track(idx + 1, sum_val + arr[idx])
    back_track(idx + 1, sum_val)

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    answer = 0

    back_track(0, 0)

    print(f'#{test_case} {answer}')