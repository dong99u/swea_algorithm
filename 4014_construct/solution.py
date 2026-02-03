import sys
sys.stdin = open('input.txt')

t = int(input())

def check(lst, n, x):
    '''
    lst가 활주로를 건설할 수 있는지 체크
    :param lst:
    :return:
    '''

    used = [False] * n  # 경사로 설치 여부 체크
    for i in range(1, n):
        # 높이가 같으면 그냥 통과
        if lst[i - 1] == lst[i]:
            continue

        # 높이 차이가 2 이상이면 애초에 활주로 못 만듦.
        if abs(lst[i - 1] - lst[i]) > 1:
            return False

        # 경우 1: 내리막 (왼쪽이 더 높음)
        # i부터 i+x-1까지 x개의 칸에 경사로 설치
        if lst[i - 1] > lst[i]:
            for j in range(i, i + x):
                # 범위를 벗어나면 경사로 설치 불가
                if j >= n:
                    return False
                # 높이가 다르면 경사로 설치 불가
                if lst[j] != lst[i]:
                    return False
                # 이미 경사로가 설치된 곳이면 불가
                if used[j]:
                    return False
                # 경사로 설치 표시
                used[j] = True

        # 경우 2: 오르막 (왼쪽이 더 낮음)
        # i-x부터 i-1까지 x개의 칸에 경사로 설치
        else:  # lst[i - 1] < lst[i]
            for j in range(i - x, i):
                # 범위를 벗어나면 경사로 설치 불가
                if j < 0:
                    return False
                # 높이가 다르면 경사로 설치 불가
                if lst[j] != lst[i - 1]:
                    return False
                # 이미 경사로가 설치된 곳이면 불가
                if used[j]:
                    return False
                # 경사로 설치 표시
                used[j] = True

    return True

for tc in range(1, t + 1):
    n, x = map(int, input().split())

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    answer = 0
    # 가로 행에 대해서 활주로 건설 여부 체크
    for lst in grid:
        if check(lst, n, x):
            answer += 1

    for lst in zip(*grid):
        if check(lst, n, x):
            answer += 1

    print(f'#{tc} {answer}')