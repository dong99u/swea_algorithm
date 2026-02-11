import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    arr.sort()

    answer = 1e9
    for i in range(n - k + 1):
        answer = min(answer, arr[i + k - 1] - arr[i])

    print(f'#{test_case} {answer}')