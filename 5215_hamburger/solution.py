import sys
sys.stdin = open('input.txt')

'''
상태 트리
                        (idx, points, calorie)
                               /    \
                        0-O   /      \ 0-X
                             /        \
                   (1, 100, 20)       (1, 0, 0)
                     /   \
                1-O /     \ 1-X
         (2, 400, 700)   (2, 100, 200)
           /  \               |          \
      2-O /    \ 2-X      2-O |           \ 2-X
(3, 650, 1000) (3, 400 700) (3, 350, 500) (2, 100, 200)
...
'''
def back_track(idx, points, calorie):
    '''
    :param idx: 현재 선택할지 안할지 고려하는 재료의 인덱스
    :param points: 현재까지 고른 재료들의 점수 총합
    :param calorie: 현재까지 고른 재료들의 칼로리 총합
    :return: 
    '''
    global answer
    if idx == n:
        answer = max(answer, points)
        return

    next_calorie = calorie + arr[idx][1]

    if  next_calorie <= l:
        back_track(idx + 1, points + arr[idx][0], next_calorie)
    back_track(idx + 1, points, calorie)

t = int(input())

for test_case in range(1, t + 1):
    # n = 재료 개수
    # l = 칼로리 제한
    n, l = map(int, input().split())

    arr = []
    for _ in range(n):
        # t = 점수
        # k = 칼로리
        t, k = map(int, input().split())
        arr.append((t, k))

    answer = 0

    back_track(0, 0, 0)

    print(f'#{test_case} {answer}')