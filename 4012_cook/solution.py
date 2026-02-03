import sys
sys.stdin = open('input.txt')

t = int(input())

def get_sum(selected):
    '''

    선택한 식재료들 n // 2 개 중에 2개씩 뽑아 그 시너지의 합을 구함
    :param selected: 선택한 식재료들 n // 2 개
    :return result: 식재료들의 시너지의 합
    '''

    result = 0
    for i in range(len(selected) - 1):
        for j in range(i + 1, len(selected)):
            ai = selected[i]
            aj = selected[j]

            result += lst[ai][aj] + lst[aj][ai]

    return result

def get_diff(selected):
    '''
    A 음식과 B 음식의 맛의 차이를 구함.
    :param selected: A 음식의 식재료들
    :return: A음식과 B음식의 맛이 차이의 절댓값
    '''
    rest = list(set(range(n)) - selected)
    selected = list(selected)

    a_sum = get_sum(selected)
    b_sum = get_sum(rest)

    return abs(a_sum - b_sum)

def dfs(start_idx, depth, selected):
    '''
    :param start_idx: 조합을 위한 시작 인덱스
    :param depth: 재귀 함수의 깊이
    :param selected: A 음식의 식재료들의 조합
    :return:
    '''

    global answer

    # basis
    if depth == n // 2:
        answer = min(answer, get_diff(selected))
        return

    for i in range(start_idx, n):
        dfs(i + 1, depth + 1, selected | {i})

for tc in range(1, t + 1):

    n = int(input())

    # 시너지
    lst = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    answer = float('inf')
    dfs(0, 0, set())

    print(f'#{tc} {answer}')