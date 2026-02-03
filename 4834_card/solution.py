import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    nums = list(map(int, input()))

    cnt = [0] * 10

    for num in nums:
        cnt[num] += 1

    max_value = -1
    max_cnt = cnt[0]

    for idx, c in enumerate(cnt):
        if max_cnt < c:
            max_cnt = c
            max_value = idx

        if max_cnt == c:
            max_value = idx


    print(f'#{tc} {max_value} {max_cnt}')