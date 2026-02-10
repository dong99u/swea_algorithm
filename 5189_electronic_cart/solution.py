import sys
sys.stdin = open('input.txt')

'''
                (curr, acc, depth)
                (1, 0, 0)
                   /  \
                  /    \
                 /      \
          (2, 18, 1)  (3, 34, 1)
           /              \
          /                \
    (3, 18+55, 2)        (2, 34+7, 2)
'''
def back_track(curr, acc, depth):
    '''
    :param curr: 현재 위치(출발 인덱스)
    :param acc: 사무실 출발부터 각 관리구역을 돌면서 사용했던 배터리의 총합
    :param depth: 상태 트리의 깊이
    :return:
    '''
    global answer

    # 모든 경우의 수(순열)을 구했을 때
    if depth == n - 1:
        # 1번 사무실부터 순열 순서로 관리구역을 돌았을 때 배터리의 총합에
        # 마지막으로 돌았던 관리구역에서 다시 1번 사무실로 돌아오는 배터리의 양을 더해야한다.
        answer = min(answer, acc + grid[curr][0])
        return

    # 어떤 관리구역 순서로 돌지 순열로 구한다.
    # 전역 visited 배열을 사용한다.
    for i in range(1, n):
        # 방문하지 않았던 관리구역이고 배터리의 사용량이 이전의 배터리 사용량보다 초과하면 최소가 될 수 없으므로
        # 그 상태는 구하지 않는다.
        if not visited[i] and acc + grid[curr][i] < answer:
            visited[i] = True
            back_track(i, acc + grid[curr][i], depth + 1)
            visited[i] = False


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    visited = [False] * n

    # 최소값을 구하기 위해 큰 수로 정의해놓는다.
    # 귀찮아서 그냥 제일 큰 값으로 했다...
    answer = 1e9
    back_track(0, 0, 0)

    print(f'#{test_case} {answer}')
