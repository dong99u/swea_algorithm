import sys
sys.stdin = open('input.txt')

def spin(arr, n, cnt):

    result = arr

    for _ in range(cnt):
        temp = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                temp[j][n - i - 1] = result[i][j]

        result = temp

    return result

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    arr = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    result1 = spin(arr, n, 1)
    result2 = spin(arr, n, 2)
    result3 = spin(arr, n, 3)


    print(f'#{tc}')
    for i in range(n):
        r1 = ''.join(map(str, result1[i]))
        r2 = ''.join(map(str, result2[i]))
        r3 = ''.join(map(str, result3[i]))
        print(f'{r1} {r2} {r3}')

